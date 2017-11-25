# kfcscrape
此项目爬取在百度地图和高德地图中搜索“南京肯德基”关键字所得到的结果，爬虫框架使用scrapy，数据存储使用Postgres数据库，大家可以根据自己需要输入不同的关键字进行爬取。
## 爬虫思路
- 抓包获取关键字请求url:
通过抓包方法分别在百度地图和高德地图中获取请求的url，以在南京市搜索关键字“南京肯德基”为例
    - 百度地图的请求地址为  
[http://map.baidu.com/?newmap=1&reqflag=pcmap&qt=con&from=webmap&c=315&wd=南京肯德基&pn=1&on_gel=1&ie=utf-8&b=(13163180.95967742,3726294.55;13290796.95967742,3762646.55)](http://map.baidu.com/?newmap=1&reqflag=pcmap&qt=con&from=webmap&c=315&wd=南京肯德基&pn=1&on_gel=1&ie=utf-8&b=(13163180.95967742,3726294.55;13290796.95967742,3762646.55))  
分析url得到结论，wd参数为输入关键字；pn参数为搜索结果的页码，b为搜索的地理范围，通过遍历pn的值获取所有搜索的结果
    - 高德地图的请求地址为  
[http://ditu.amap.com/service/poiInfo?query_type=TQUERY&pagesize=20&pagenum=&need_utd=true&utd_sceneid=1000&city=320100&geoobj=118.694927|32.024763|119.009067|32.117861&keywords=南京肯德基](http://ditu.amap.com/service/poiInfo?query_type=TQUERY&pagesize=20&pagenum=1&need_utd=true&utd_sceneid=1000&city=320100&geoobj=118.694927|32.024763|119.009067|32.117861&keywords=南京肯德基)  
分析url得出结论，city参数为搜索城市的代码，geoobj参数为搜索的地理范围，keywords为搜索关键字，pagenum为搜索结果的页码，通过遍历pagenum的值获取所有搜索结果。
- 分析抓包结果内容构造Item
抓包的结果都是json格式的数据，
百度地图搜索结果在content对象中，高德地图搜索结果在data对象的poi_list对象中，根据自身需要构建Item类。
    - 百度地图Item类：  
    ```
    class baidukfcItem(scrapy.Item):
    id = scrapy.Field()
    addr = scrapy.Field()
    address_norm = scrapy.Field()
    alias = scrapy.Field()
    aoi = scrapy.Field()
    area_name = scrapy.Field()
    diPointX = scrapy.Field()
    diPointY = scrapy.Field()
    tag = scrapy.Field()
    name = scrapy.Field()
    std_tag = scrapy.Field()
    tel = scrapy.Field()
    cater_tag = scrapy.Field()
    comment_num = scrapy.Field()
    overall_rating = scrapy.Field()
    price = scrapy.Field()
    ```
    - 高德地图Item类：  
    ```
    class amapkfcItem(scrapy.Item):
    id = scrapy.Field()
    rating = scrapy.Field()
    tel = scrapy.Field()
    cityname = scrapy.Field()
    address = scrapy.Field()
    adcode = scrapy.Field()
    name = scrapy.Field()
    latitude = scrapy.Field()
    longitude = scrapy.Field()
    tag = scrapy.Field()
    business_area = scrapy.Field()
    price = scrapy.Field()
    aoi = scrapy.Field()
    ```
- 解析抓包结果获得爬取值
在spider文件夹中创建两个spider文件，分别编写百度地图和高德地图的spider。通过直接获取搭配xpath的方法解析json的结构，将解析得到的值填充Item，保存获取到的值。  
**Tips：** 在获取json的某一对象时，有些对象不存在，例如想要获取某条数据的address值，但该条数据中根本不存在address这条标签，这样可能会导致爬虫中断，因此做一个if判断，如果该标签不存在，则在该条Item中设置该对象的值为空，如下所示：  
    ```
    item['address'] = object['address'] if 'address' in object else ""
    ```  
    这样保证了爬虫的连贯与完整。
- 编写pipelines连接数据库  
本爬虫使用postgres数据库，引入psycopg2包，修改psycopg2.connect方法中的参数，配置自己的postgres数据库连接。本爬虫中有两个spider，通过判断spider.name执行不同的数据库连接。如下图所示，修改该方法中xxx的参数：  
    ```
    conn = psycopg2.connect(database='xxx', user='xxx', password='xxx', host='xxx', port='5432')
    ```  
    本爬虫中有两个spider，通过判断spider.name执行不同的数据库连接。  
    ```
    if spider.name == 'baidukfc':
        ...
    elif spider.name == 'amapkfc':
        ...
    ```  
    在settings中将ITEM_PIPELINES属性去除注释。  
    ```
    ITEM_PIPELINES = {
    'kfcscrape.pipelines.KfcscrapePipeline': 300,
    }
    ```  
- 执行爬虫
OK！只需要执行两个spider就可以得到数据了！  
**Tips:** 为了不被网站的反爬虫系统和谐，我们在settings中设置一下DOWNLOAD_DELAY，以控制访问请求的事件间隔。  
    ```
    DOWNLOAD_DELAY = 3
    ```
## 结果图
![bmap](http://oswrmk9hd.bkt.clouddn.com/%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202017-11-25%20%E4%B8%8B%E5%8D%8810.27.32.png)  
![amap](http://oswrmk9hd.bkt.clouddn.com/%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202017-11-25%20%E4%B8%8B%E5%8D%8810.28.25.png)
## 联系我们
E-mail: 535848615@qq.com  
博客园：[http://www.cnblogs.com/KloseJiao/](http://www.cnblogs.com/KloseJiao/)  
欢迎留言和邮件与我交流！