# Pagination 

<p><img src="https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2019/12/3646eb02de6527ca5d83.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20240109%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20240109T140925Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=007ae4ebfdc6de97f129192b2f78ed12fe7e03e054985969dc3eec50333cac29" alt="" loading='lazy' style="" />
<img src="https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2019/12/746187b76bea1f46030e.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20240109%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20240109T140925Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=dde0f47c5bdeee90943f5dd7083578b4ce8e3e2a5d58e5a822fc90cf35d457b2" alt="" loading='lazy' style="" />
<img src="https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2019/12/665ce871c2ecc66a8e71.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20240109%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20240109T140925Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=94167e611a1a1d5ee1da5a679d52f8cfabdc9d1fd80e3b25d2a06465e52b3e22" alt="" loading='lazy' style="" /></p>

<h2>Resources</h2>

<p><strong>Read or watch:</strong></p>

<ul>
<li><a href="/rltoken/VeL1Cbu_NVNND6WKJrECbg" title="REST API Design: Pagination" target="_blank">REST API Design: Pagination</a></li>
<li><a href="/rltoken/Mqk-KBxLRtJaQuWZO-oeAQ" title="HATEOAS" target="_blank">HATEOAS</a></li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/cTaCEqXO09xize9ePftDXg" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<ul>
<li>How to paginate a dataset with simple page and page_size parameters</li>
<li>How to paginate a dataset with hypermedia metadata</li>
<li>How to paginate in a deletion-resilient manner</li>
</ul>

<h2>Requirements</h2>

<ul>
<li>All your files will be interpreted/compiled on Ubuntu 18.04 LTS using <code>python3</code> (version 3.7)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/env python3</code></li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should use the <code>pycodestyle</code> style (version 2.5.*)</li>
<li>The length of your files will be tested using <code>wc</code></li>
<li>All your modules should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).__doc__)&#39;</code>)</li>
<li>All your functions should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).my_function.__doc__)&#39;</code></li>
<li>A documentation is not a simple word, it&rsquo;s a real sentence explaining what&rsquo;s the purpose of the module, class or method (the length of it will be verified)</li>
<li>All your functions and coroutines must be type-annotated.</li>
</ul>

<h2>Setup: <code>Popular_Baby_Names.csv</code></h2>

<p><a href="/rltoken/7IKLZ7i4pO4MJ9CQoGHfVw" title="use this data file" target="_blank">use this data file</a> for your project</p>


<details>
<summary>Click to see: Tasks</summary>

<h3 class="panel-title">
0. Simple helper function
</h3>

Write a function named <code>index_range</code> that takes two integer arguments <code>page</code> and <code>page_size</code>.</p>

<p>The function should return a tuple of size two containing a start index and an end index corresponding to the range of indexes to return in a list for those particular pagination parameters.</p>

<p>Page numbers are 1-indexed, i.e. the first page is page 1.</p>

<pre><code>bob@dylan:~$ cat 0-main.py
#!/usr/bin/env python3
&quot;&quot;&quot;
Main file
&quot;&quot;&quot;

index_range = __import__(&#39;0-simple_helper_function&#39;).index_range

res = index_range(1, 7)
print(type(res))
print(res)

res = index_range(page=3, page_size=15)
print(type(res))
print(res)

bob@dylan:~$ ./0-main.py
&lt;class &#39;tuple&#39;&gt;
(0, 7)
&lt;class &#39;tuple&#39;&gt;
(30, 45)
bob@dylan:~$
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-web_back_end</code></li>
<li>Directory: <code>pagination</code></li>
<li>File: <code>0-simple_helper_function.py</code></li>
</ul>
</div>

<h3 class="panel-title">
1. Simple pagination
</h3>

Copy <code>index_range</code> from the previous task and the following class into your code</p>

<pre><code>import csv
import math
from typing import List


class Server:
&quot;&quot;&quot;Server class to paginate a database of popular baby names.
&quot;&quot;&quot;
DATA_FILE = &quot;Popular_Baby_Names.csv&quot;

def __init__(self):
self.__dataset = None

def dataset(self) -&gt; List[List]:
&quot;&quot;&quot;Cached dataset
&quot;&quot;&quot;
if self.__dataset is None:
with open(self.DATA_FILE) as f:
reader = csv.reader(f)
dataset = [row for row in reader]
self.__dataset = dataset[1:]

return self.__dataset

def get_page(self, page: int = 1, page_size: int = 10) -&gt; List[List]:
pass
</code></pre>

<p>Implement a method named <code>get_page</code> that takes two integer arguments <code>page</code> with default value 1 and <code>page_size</code> with default value 10.</p>

<ul>
<li>You have to use this <a href="/rltoken/7IKLZ7i4pO4MJ9CQoGHfVw" title="CSV file" target="_blank">CSV file</a> (same as the one presented at the top of the project)</li>
<li>Use <code>assert</code> to verify that both arguments are integers greater than 0.</li>
<li>Use <code>index_range</code> to find the correct indexes to paginate the dataset correctly and return the appropriate page of the dataset (i.e. the correct list of rows).</li>
<li>If the input arguments are out of range for the dataset, an empty list should be returned.</li>
</ul>

<pre><code>bob@dylan:~$  wc -l Popular_Baby_Names.csv
19419 Popular_Baby_Names.csv
bob@dylan:~$
bob@dylan:~$ head Popular_Baby_Names.csv
Year of Birth,Gender,Ethnicity,Child&#39;s First Name,Count,Rank
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Olivia,172,1
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Chloe,112,2
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Sophia,104,3
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Emma,99,4
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Emily,99,4
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Mia,79,5
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Charlotte,59,6
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Sarah,57,7
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Isabella,56,8
bob@dylan:~$
bob@dylan:~$  cat 1-main.py
#!/usr/bin/env python3
&quot;&quot;&quot;
Main file
&quot;&quot;&quot;

Server = __import__(&#39;1-simple_pagination&#39;).Server

server = Server()

try:
should_err = server.get_page(-10, 2)
except AssertionError:
print(&quot;AssertionError raised with negative values&quot;)

try:
should_err = server.get_page(0, 0)
except AssertionError:
print(&quot;AssertionError raised with 0&quot;)

try:
should_err = server.get_page(2, &#39;Bob&#39;)
except AssertionError:
print(&quot;AssertionError raised when page and/or page_size are not ints&quot;)


print(server.get_page(1, 3))
print(server.get_page(3, 2))
print(server.get_page(3000, 100))

bob@dylan:~$
bob@dylan:~$ ./1-main.py
AssertionError raised with negative values
AssertionError raised with 0
AssertionError raised when page and/or page_size are not ints
[[&#39;2016&#39;, &#39;FEMALE&#39;, &#39;ASIAN AND PACIFIC ISLANDER&#39;, &#39;Olivia&#39;, &#39;172&#39;, &#39;1&#39;], [&#39;2016&#39;, &#39;FEMALE&#39;, &#39;ASIAN AND PACIFIC ISLANDER&#39;, &#39;Chloe&#39;, &#39;112&#39;, &#39;2&#39;], [&#39;2016&#39;, &#39;FEMALE&#39;, &#39;ASIAN AND PACIFIC ISLANDER&#39;, &#39;Sophia&#39;, &#39;104&#39;, &#39;3&#39;]]
[[&#39;2016&#39;, &#39;FEMALE&#39;, &#39;ASIAN AND PACIFIC ISLANDER&#39;, &#39;Emily&#39;, &#39;99&#39;, &#39;4&#39;], [&#39;2016&#39;, &#39;FEMALE&#39;, &#39;ASIAN AND PACIFIC ISLANDER&#39;, &#39;Mia&#39;, &#39;79&#39;, &#39;5&#39;]]
[]
bob@dylan:~$
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-web_back_end</code></li>
<li>Directory: <code>pagination</code></li>
<li>File: <code>1-simple_pagination.py</code></li>
</ul>
</div>

<h3 class="panel-title">
2. Hypermedia pagination
</h3>

Replicate code from the previous task.</p>

<p>Implement a <code>get_hyper</code> method that takes the same arguments (and defaults) as <code>get_page</code> and returns a dictionary containing the following key-value pairs:</p>

<ul>
<li><code>page_size</code>: the length of the returned dataset page</li>
<li><code>page</code>: the current page number</li>
<li><code>data</code>: the dataset page (equivalent to return from previous task)</li>
<li><code>next_page</code>: number of the next page, <code>None</code> if no next page</li>
<li><code>prev_page</code>: number of the previous page, <code>None</code> if no previous page</li>
<li><code>total_pages</code>: the total number of pages in the dataset as an integer</li>
</ul>

<p>Make sure to reuse <code>get_page</code> in your implementation. </p>

<p>You can use the <code>math</code> module if necessary.</p>

<pre><code>bob@dylan:~$ cat 2-main.py
#!/usr/bin/env python3
&quot;&quot;&quot;
Main file
&quot;&quot;&quot;

Server = __import__(&#39;2-hypermedia_pagination&#39;).Server

server = Server()

print(server.get_hyper(1, 2))
print(&quot;---&quot;)
print(server.get_hyper(2, 2))
print(&quot;---&quot;)
print(server.get_hyper(100, 3))
print(&quot;---&quot;)
print(server.get_hyper(3000, 100))

bob@dylan:~$
bob@dylan:~$ ./2-main.py
{&#39;page_size&#39;: 2, &#39;page&#39;: 1, &#39;data&#39;: [[&#39;2016&#39;, &#39;FEMALE&#39;, &#39;ASIAN AND PACIFIC ISLANDER&#39;, &#39;Olivia&#39;, &#39;172&#39;, &#39;1&#39;], [&#39;2016&#39;, &#39;FEMALE&#39;, &#39;ASIAN AND PACIFIC ISLANDER&#39;, &#39;Chloe&#39;, &#39;112&#39;, &#39;2&#39;]], &#39;next_page&#39;: 2, &#39;prev_page&#39;: None, &#39;total_pages&#39;: 9709}
---
{&#39;page_size&#39;: 2, &#39;page&#39;: 2, &#39;data&#39;: [[&#39;2016&#39;, &#39;FEMALE&#39;, &#39;ASIAN AND PACIFIC ISLANDER&#39;, &#39;Sophia&#39;, &#39;104&#39;, &#39;3&#39;], [&#39;2016&#39;, &#39;FEMALE&#39;, &#39;ASIAN AND PACIFIC ISLANDER&#39;, &#39;Emma&#39;, &#39;99&#39;, &#39;4&#39;]], &#39;next_page&#39;: 3, &#39;prev_page&#39;: 1, &#39;total_pages&#39;: 9709}
---
{&#39;page_size&#39;: 3, &#39;page&#39;: 100, &#39;data&#39;: [[&#39;2016&#39;, &#39;FEMALE&#39;, &#39;BLACK NON HISPANIC&#39;, &#39;Londyn&#39;, &#39;14&#39;, &#39;39&#39;], [&#39;2016&#39;, &#39;FEMALE&#39;, &#39;BLACK NON HISPANIC&#39;, &#39;Amirah&#39;, &#39;14&#39;, &#39;39&#39;], [&#39;2016&#39;, &#39;FEMALE&#39;, &#39;BLACK NON HISPANIC&#39;, &#39;McKenzie&#39;, &#39;14&#39;, &#39;39&#39;]], &#39;next_page&#39;: 101, &#39;prev_page&#39;: 99, &#39;total_pages&#39;: 6473}
---
{&#39;page_size&#39;: 0, &#39;page&#39;: 3000, &#39;data&#39;: [], &#39;next_page&#39;: None, &#39;prev_page&#39;: 2999, &#39;total_pages&#39;: 195}
bob@dylan:~$
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-web_back_end</code></li>
<li>Directory: <code>pagination</code></li>
<li>File: <code>2-hypermedia_pagination.py</code></li>
</ul>
</div>

<h3 class="panel-title">
3. Deletion-resilient hypermedia pagination
</h3>

The goal here is that if between two queries, certain rows are removed from the dataset, the user does not miss items from dataset when changing page.</p>

<p>Start <code>3-hypermedia_del_pagination.py</code> with this code:</p>

<pre><code>#!/usr/bin/env python3
&quot;&quot;&quot;
Deletion-resilient hypermedia pagination
&quot;&quot;&quot;

import csv
import math
from typing import List


class Server:
&quot;&quot;&quot;Server class to paginate a database of popular baby names.
&quot;&quot;&quot;
DATA_FILE = &quot;Popular_Baby_Names.csv&quot;

def __init__(self):
self.__dataset = None
self.__indexed_dataset = None

def dataset(self) -&gt; List[List]:
&quot;&quot;&quot;Cached dataset
&quot;&quot;&quot;
if self.__dataset is None:
with open(self.DATA_FILE) as f:
reader = csv.reader(f)
dataset = [row for row in reader]
self.__dataset = dataset[1:]

return self.__dataset

def indexed_dataset(self) -&gt; Dict[int, List]:
&quot;&quot;&quot;Dataset indexed by sorting position, starting at 0
&quot;&quot;&quot;
if self.__indexed_dataset is None:
dataset = self.dataset()
truncated_dataset = dataset[:1000]
self.__indexed_dataset = {
i: dataset[i] for i in range(len(dataset))
}
return self.__indexed_dataset

def get_hyper_index(self, index: int = None, page_size: int = 10) -&gt; Dict:
pass
</code></pre>

<p>Implement a <code>get_hyper_index</code> method with two integer arguments: <code>index</code> with a <code>None</code> default value and <code>page_size</code> with default value of 10.</p>

<ul>
<li>The method should return a dictionary with the following key-value pairs:

<ul>
<li><code>index</code>: the current start index of the return page. That is the index of the first item in the current page. For example if requesting page 3 with <code>page_size</code> 20, and no data was removed from the dataset, the current index should be 60.</li>
<li><code>next_index</code>: the next index to query with. That should be the index of the first item after the last item on the current page.</li>
<li><code>page_size</code>: the current page size</li>
<li><code>data</code>: the actual page of the dataset</li>
</ul></li>
</ul>

<p><strong>Requirements/Behavior</strong>:</p>

<ul>
<li>Use <code>assert</code> to verify that <code>index</code> is in a valid range.</li>
<li>If the user queries index 0, <code>page_size</code> 10, they will get rows indexed 0 to 9 included. </li>
<li>If they request the next index (10) with <code>page_size</code> 10, but rows 3, 6 and 7 were deleted, the user should still receive rows indexed 10 to 19 included.</li>
</ul>

<pre><code>bob@dylan:~$ cat 3-main.py
#!/usr/bin/env python3
&quot;&quot;&quot;
Main file
&quot;&quot;&quot;

Server = __import__(&#39;3-hypermedia_del_pagination&#39;).Server

server = Server()

server.indexed_dataset()

try:
server.get_hyper_index(300000, 100)
except AssertionError:
print(&quot;AssertionError raised when out of range&quot;)


index = 3
page_size = 2

print(&quot;Nb items: {}&quot;.format(len(server._Server__indexed_dataset)))

# 1- request first index
res = server.get_hyper_index(index, page_size)
print(res)

# 2- request next index
print(server.get_hyper_index(res.get(&#39;next_index&#39;), page_size))

# 3- remove the first index
del server._Server__indexed_dataset[res.get(&#39;index&#39;)]
print(&quot;Nb items: {}&quot;.format(len(server._Server__indexed_dataset)))

# 4- request again the initial index -&gt; the first data retreives is not the same as the first request
print(server.get_hyper_index(index, page_size))

# 5- request again initial next index -&gt; same data page as the request 2-
print(server.get_hyper_index(res.get(&#39;next_index&#39;), page_size))

bob@dylan:~$
bob@dylan:~$ ./3-main.py
AssertionError raised when out of range
Nb items: 19418
{&#39;index&#39;: 3, &#39;data&#39;: [[&#39;2016&#39;, &#39;FEMALE&#39;, &#39;ASIAN AND PACIFIC ISLANDER&#39;, &#39;Emma&#39;, &#39;99&#39;, &#39;4&#39;], [&#39;2016&#39;, &#39;FEMALE&#39;, &#39;ASIAN AND PACIFIC ISLANDER&#39;, &#39;Emily&#39;, &#39;99&#39;, &#39;4&#39;]], &#39;page_size&#39;: 2, &#39;next_index&#39;: 5}
{&#39;index&#39;: 5, &#39;data&#39;: [[&#39;2016&#39;, &#39;FEMALE&#39;, &#39;ASIAN AND PACIFIC ISLANDER&#39;, &#39;Mia&#39;, &#39;79&#39;, &#39;5&#39;], [&#39;2016&#39;, &#39;FEMALE&#39;, &#39;ASIAN AND PACIFIC ISLANDER&#39;, &#39;Charlotte&#39;, &#39;59&#39;, &#39;6&#39;]], &#39;page_size&#39;: 2, &#39;next_index&#39;: 7}
Nb items: 19417
{&#39;index&#39;: 3, &#39;data&#39;: [[&#39;2016&#39;, &#39;FEMALE&#39;, &#39;ASIAN AND PACIFIC ISLANDER&#39;, &#39;Emily&#39;, &#39;99&#39;, &#39;4&#39;], [&#39;2016&#39;, &#39;FEMALE&#39;, &#39;ASIAN AND PACIFIC ISLANDER&#39;, &#39;Mia&#39;, &#39;79&#39;, &#39;5&#39;]], &#39;page_size&#39;: 2, &#39;next_index&#39;: 6}
{&#39;index&#39;: 5, &#39;data&#39;: [[&#39;2016&#39;, &#39;FEMALE&#39;, &#39;ASIAN AND PACIFIC ISLANDER&#39;, &#39;Mia&#39;, &#39;79&#39;, &#39;5&#39;], [&#39;2016&#39;, &#39;FEMALE&#39;, &#39;ASIAN AND PACIFIC ISLANDER&#39;, &#39;Charlotte&#39;, &#39;59&#39;, &#39;6&#39;]], &#39;page_size&#39;: 2, &#39;next_index&#39;: 7}
bob@dylan:~$
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-web_back_end</code></li>
<li>Directory: <code>pagination</code></li>
<li>File: <code>3-hypermedia_del_pagination.py</code></li>
</ul>
</div>

</details>
