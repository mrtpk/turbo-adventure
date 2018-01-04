import re





'''
input:
![image caption]("alt text" 'path for the image')
output:
<div class="image">
    <img src='link to random picture' alt="some random picture"><br>
    <span class="caption">A sample picture</span>
</div>
'''
def putImageTag(corpus):
    regex = r'\!\[(.*)\]\(\"(.*)\" \'(.*)\'\)'
    imageTag = r'''<div class="image">
    <img src='\3' alt="\2"><br>
    <span class="caption">\1</span>
</div>\n'''
    return re.sub(regex,imageTag,corpus)

'''
@input
![ref]("link text" 'link')
@output
<a href='link to href'>href</a>
'''
def putAnchorTags(corpus):
    regex = r'\!\[ref\]\(\"(.*)\" \'(.*)\'\)'
    anchorTag = r'''<a href='\2'>\1</a>'''
    return re.sub(regex,anchorTag,corpus)

'''
@input
![title]("A sample input for processing" "November 8 2017")
@output
<div class="title">
    <h1>A sample input for processing</h1>
    <span class="tag">November 8 2017</span>
</div>
'''
def putTilte(corpus):
    regex = r'\!\[title\]\(\"(.*)\" \"(.*)\"\)'
    titleTag = r'''<div class="title">
	<h1>\1</h1>
	<span class="tag">\2</span>
</div>\n<div class="body">\n'''
    return re.sub(regex,titleTag,corpus) + '\n<div>\n'


def putParagraph(corpus):
    regex = r'''\n\s*\n(.*)'''
    paragraphTag = r'''\n<p>\1</p>\n'''
    return re.sub(regex,paragraphTag,corpus)

def putH1Tag(corpus):
    regex = r'''\n?!>(.*)\n'''
    h1Tag = r'''<h1>\1</h1>\n'''
    return re.sub(regex,h1Tag,corpus)
def putH2Tag(corpus):
    regex = r'''\n?!>>(.*)\n'''
    h2Tag = r'''<h2>\1</h2>\n'''
    return re.sub(regex,h2Tag,corpus)
def putH3Tag(corpus):
    regex = r'''\n?!>>>(.*)\n'''
    h1Tag = r'''<h3>\1</h3>\n'''
    return re.sub(regex,h1Tag,corpus)

def makePost(corpus):
    post = '''<div class="post">
    '''+corpus+'''<div>'''
    return post


corpus = '''![title]("A HTML converter in python" "November 9 2017")
![A sample picture]("some random picture" 'random.jpg')

This python program converts text file like this to HTML page. This was done to writing easily. A paragraph is started by leaving a blank line; like this one. A paragraph is a line followed by a blank line.

!>>Headers are shown using \!\>\>. This is a H2 header

This python program converts text file like this to HTML page. This was done to make writing easy. A paragraph is started by leaving a blank line; like this one. A paragraph is a line followed by a blank line.![ref]("href" 'http://localhost:8000/blog.html')

This python program converts text file like this to HTML page. This was done to make writing easy. A paragraph is started by leaving a blank line; like this one. A paragraph is a line followed by a blank line.

![A sample picture]("some random picture" 'random.jpg')
'''
corpus = putH1Tag(putH2Tag(putH3Tag(corpus)))
#print("after h tags :", corpus)
corpus = putParagraph(corpus)
corpus = putTilte(corpus)
#print("After paragraph :", corpus)
corpus = putAnchorTags(corpus)
corpus = putImageTag(corpus)

#print('after title tags :', corpus)
corpus = makePost(corpus)
print("HTML\n====")
print(corpus)

