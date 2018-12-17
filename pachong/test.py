from pyquery import PyQuery as pq
html = '''
    <div id="wrap">
        <ul class="s_from">
            asdasd
            <link href="http://asda.com">asdadasdad12312</link>
            <link href="http://asda1.com">asdadasdad12312</link>
            <link href="http://asda2.com">asdadasdad12312</link>
        </ul>
    </div>
'''
doc = pq(html)
print(doc("#wrap .s_from link"))