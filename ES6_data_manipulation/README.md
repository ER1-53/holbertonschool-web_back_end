# ES6 data manipulation

<p><img src="https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2019/12/6ab7bec4727cb5c91257.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20240129%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20240129T091241Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=7a5c77492233e30462bf8779f5bca0cf5240e98aa83789386a394b3a8eb40749" alt="" loading='lazy' style="" /></p>

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/fXeF-M30vPa-VR4qdM1hbQ" title="Array" target="_blank">Array</a></li>
<li><a href="/rltoken/K8YavMi9P0JsBDS4W8PXvw" title="Typed Array" target="_blank">Typed Array</a></li>
<li><a href="/rltoken/47KxkohflmsBUjMCzRxMkQ" title="Set Data Structure" target="_blank">Set Data Structure</a></li>
<li><a href="/rltoken/c01xzbbE1CXwbXEW8jS0gQ" title="Map Data Structure" target="_blank">Map Data Structure</a></li>
<li><a href="/rltoken/f-CLehBUa4LvtJt5c_tEUw" title="WeakMap" target="_blank">WeakMap</a></li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/zzHjkh9ju_sW7hoJXB_gfQ" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<ul>
<li>How to use map, filter and reduce on arrays</li>
<li>Typed arrays</li>
<li>The Set, Map, and Weak link data structures</li>
</ul>

<h2>Requirements</h2>

<ul>
<li>All your files will be executed on Ubuntu 18.04 LTS using NodeJS 12.11.x</li>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code>, <code>Visual Studio Code</code></li>
<li>All your files should end with a new line</li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should use the <code>js</code> extension</li>
<li>Your code will be tested using <code>Jest</code> and the command <code>npm run test</code></li>
<li>Your code will be verified against lint using ESLint</li>
<li>Your code needs to pass all the tests and lint. You can verify the entire project running <code>npm run full-test</code></li>
<li>All of your functions must be exported</li>
</ul>

<h2>Setup</h2>

<h3>Install NodeJS 12.11.x</h3>

<p>(in your home directory): </p>

<pre><code>curl -sL https://deb.nodesource.com/setup_12.x -o nodesource_setup.sh
sudo bash nodesource_setup.sh
sudo apt install nodejs -y
</code></pre>

<pre><code>$ nodejs -v
v12.11.1
$ npm -v
6.11.3
</code></pre>

<h3>Install Jest, Babel, and ESLint</h3>

<p>in your project directory: </p>

<ul>
<li>Install Jest using: <code>npm install --save-dev jest</code></li>
<li>Install Babel using: <code>npm install --save-dev babel-jest @babel/core @babel/preset-env</code></li>
<li>Install ESLint using: <code>npm install --save-dev eslint</code></li>
</ul>

<h2>Configuration files</h2>

<h3><code>package.json</code></h3>

<details>
<summary>Click to show/hide file contents</summary>
<pre>
<code>
{
"scripts": {
"lint": "./node_modules/.bin/eslint",
"check-lint": "lint [0-9]*.js",
"dev": "npx babel-node",
"test": "jest",
"full-test": "./node_modules/.bin/eslint [0-9]*.js && jest"
},
"devDependencies": {
"@babel/core": "^7.6.0",
"@babel/node": "^7.8.0",
"@babel/preset-env": "^7.6.0",
"eslint": "^6.4.0",
"eslint-config-airbnb-base": "^14.0.0",
"eslint-plugin-import": "^2.18.2",
"eslint-plugin-jest": "^22.17.0",
"jest": "^24.9.0"
}
}
</code>
</pre>
</details>

<h3><code>babel.config.js</code></h3>

<details>
<summary>Click to show/hide file contents</summary>
<pre>
<code>
module.exports = {
presets: [
[
'@babel/preset-env',
{
targets: {
node: 'current',
},
},
],
],
};
</code>
</pre>
</details>

<h3><code>.eslintrc.js</code></h3>

<details>
<summary>Click to show/hide file contents</summary>
<pre>
<code>
module.exports = {
env: {
browser: false,
es6: true,
jest: true,
},
extends: [
'airbnb-base',
'plugin:jest/all',
],
globals: {
Atomics: 'readonly',
SharedArrayBuffer: 'readonly',
},
parserOptions: {
ecmaVersion: 2018,
sourceType: 'module',
},
plugins: ['jest'],
rules: {
'max-classes-per-file': 'off',
'no-underscore-dangle': 'off',
'no-console': 'off',
'no-shadow': 'off',
'no-restricted-syntax': [
'error',
'LabeledStatement',
'WithStatement',
],
},
overrides:[
{
files: ['*.js'],
excludedFiles: 'babel.config.js',
}
]
};
</code>
</pre>
</details>

<h3>and&hellip;</h3>

<p>Don&rsquo;t forget to run <code>$ npm install</code> when you have the <code>package.json</code></p>


<details>
<summary>Click to see: Tasks</summary>

<h3 class="panel-title">
0. Basic list of objects
</h3>

Create a function named <code>getListStudents</code> that returns an array of objects. </p>

<p>Each object should have three attributes: <code>id</code> (Number), <code>firstName</code> (String), and <code>location</code> (String). </p>

<p>The array contains the following students in order: </p>

<ul>
<li><code>Guillaume</code>, id: <code>1</code>, in <code>San Francisco</code></li>
<li><code>James</code>, id: <code>2</code>, in <code>Columbia</code></li>
<li><code>Serena</code>, id: <code>5</code>, in <code>San Francisco</code></li>
</ul>

<pre><code>bob@dylan:~$ cat 0-main.js
import getListStudents from &quot;./0-get_list_students.js&quot;;

console.log(getListStudents());

bob@dylan:~$
bob@dylan:~$ npm run dev 0-main.js
[
{ id: 1, firstName: &#39;Guillaume&#39;, location: &#39;San Francisco&#39; },
{ id: 2, firstName: &#39;James&#39;, location: &#39;Columbia&#39; },
{ id: 5, firstName: &#39;Serena&#39;, location: &#39;San Francisco&#39; }
]
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
<li>Directory: <code>ES6_data_manipulation</code></li>
<li>File: <code>0-get_list_students.js</code></li>
</ul>
</div>

<h3 class="panel-title">
1. More mapping
</h3>

Create a function <code>getListStudentIds</code> that returns an array of ids from a list of object.</p>

<p>This function is taking one argument which is an array of objects - and this array is the same format as <code>getListStudents</code> from the previous task.</p>

<p>If the argument is not an array, the function is returning an empty array.</p>

<p>You must use the <code>map</code> function on the array.</p>

<pre><code>bob@dylan:~$ cat 1-main.js
import getListStudentIds from &quot;./1-get_list_student_ids.js&quot;;
import getListStudents from &quot;./0-get_list_students.js&quot;;

console.log(getListStudentIds(&quot;hello&quot;));
console.log(getListStudentIds(getListStudents()));

bob@dylan:~$
bob@dylan:~$ npm run dev 1-main.js
[]
[ 1, 2, 5 ]
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
<li>Directory: <code>ES6_data_manipulation</code></li>
<li>File: <code>1-get_list_student_ids.js</code></li>
</ul>
</div>

<h3 class="panel-title">
2. Filter
</h3>

Create a function <code>getStudentsByLocation</code> that returns an array of objects who are located in a specific city.</p>

<p>It should accept a list of students (from <code>getListStudents</code>) and a <code>city</code> (string) as parameters.</p>

<p>You must use the <code>filter</code> function on the array.</p>

<pre><code>bob@dylan:~$ cat 2-main.js
import getListStudents from &quot;./0-get_list_students.js&quot;;
import getStudentsByLocation from &quot;./2-get_students_by_loc.js&quot;;

const students = getListStudents();

console.log(getStudentsByLocation(students, &#39;San Francisco&#39;));

bob@dylan:~$
bob@dylan:~$ npm run dev 2-main.js
[
{ id: 1, firstName: &#39;Guillaume&#39;, location: &#39;San Francisco&#39; },
{ id: 5, firstName: &#39;Serena&#39;, location: &#39;San Francisco&#39; }
]
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
<li>Directory: <code>ES6_data_manipulation</code></li>
<li>File: <code>2-get_students_by_loc.js</code></li>
</ul>
</div>

<h3 class="panel-title">
3. Reduce
</h3>

Create a function <code>getStudentIdsSum</code> that returns the sum of all the student ids.</p>

<p>It should accept a list of students (from <code>getListStudents</code>) as a parameter. </p>

<p>You must use the <code>reduce</code> function on the array. </p>

<pre><code>bob@dylan:~$ cat 3-main.js
import getListStudents from &quot;./0-get_list_students.js&quot;;
import getStudentIdsSum from &quot;./3-get_ids_sum.js&quot;;

const students = getListStudents();
const value = getStudentIdsSum(students);

console.log(value);

bob@dylan:~$
bob@dylan:~$ npm run dev 3-main.js
8
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
<li>Directory: <code>ES6_data_manipulation</code></li>
<li>File: <code>3-get_ids_sum.js</code></li>
</ul>
</div>

<h3 class="panel-title">
4. Combine
</h3>

Create a function <code>updateStudentGradeByCity</code> that returns an array of students for a specific city with their new grade</p>

<p>It should accept a list of students (from <code>getListStudents</code>), a <code>city</code> (String), and <code>newGrades</code> (Array of &ldquo;grade&rdquo; objects) as parameters. </p>

<p><code>newGrades</code> is an array of objects with this format:</p>

<pre><code>  {
studentId: 31,
grade: 78,
}
</code></pre>

<p>If a student doesn&rsquo;t have grade in <code>newGrades</code>, the final grade should be <code>N/A</code>.</p>

<p>You must use <code>filter</code> and <code>map</code> combined.</p>

<pre><code>bob@dylan:~$ cat 4-main.js
import getListStudents from &quot;./0-get_list_students.js&quot;;
import updateStudentGradeByCity from &quot;./4-update_grade_by_city.js&quot;;

console.log(updateStudentGradeByCity(getListStudents(), &quot;San Francisco&quot;, [{ studentId: 5, grade: 97 }, { studentId: 1, grade: 86 }]));

console.log(updateStudentGradeByCity(getListStudents(), &quot;San Francisco&quot;, [{ studentId: 5, grade: 97 }]));

bob@dylan:~$
bob@dylan:~$ npm run dev 4-main.js
[
{
id: 1,
firstName: &#39;Guillaume&#39;,
location: &#39;San Francisco&#39;,
grade: 86
},
{ id: 5, firstName: &#39;Serena&#39;, location: &#39;San Francisco&#39;, grade: 97 }
]
[
{
id: 1,
firstName: &#39;Guillaume&#39;,
location: &#39;San Francisco&#39;,
grade: &#39;N/A&#39;
},
{ id: 5, firstName: &#39;Serena&#39;, location: &#39;San Francisco&#39;, grade: 97 }
]
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
<li>Directory: <code>ES6_data_manipulation</code></li>
<li>File: <code>4-update_grade_by_city.js</code></li>
</ul>
</div>

<h3 class="panel-title">
5. Typed Arrays
</h3>

Create a function named <code>createInt8TypedArray</code> that returns a new <code>ArrayBuffer</code> with an <code>Int8</code> value at a specific position.</p>

<p>It should accept three arguments: <code>length</code> (Number), <code>position</code> (Number), and <code>value</code> (Number).</p>

<p>If adding the value is not possible the error <code>Position outside range</code> should be thrown.</p>

<pre><code>bob@dylan:~$ cat 5-main.js
import createInt8TypedArray from &quot;./5-typed_arrays.js&quot;;

console.log(createInt8TypedArray(10, 2, 89));

bob@dylan:~$
bob@dylan:~$ npm run dev 5-main.js
DataView {
byteLength: 10,
byteOffset: 0,
buffer: ArrayBuffer {
[Uint8Contents]: &lt;00 00 59 00 00 00 00 00 00 00&gt;,
byteLength: 10
}
}
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
<li>Directory: <code>ES6_data_manipulation</code></li>
<li>File: <code>5-typed_arrays.js</code></li>
</ul>
</div>

<h3 class="panel-title">
6. Set data structure
</h3>

Create a function named <code>setFromArray</code> that returns a <code>Set</code> from an array.</p>

<p>It accepts an argument (Array, of any kind of element). </p>

<pre><code>bob@dylan:~$ cat 6-main.js
import setFromArray from &quot;./6-set.js&quot;;

console.log(setFromArray([12, 32, 15, 78, 98, 15]));

bob@dylan:~$
bob@dylan:~$ npm run dev 6-main.js
Set { 12, 32, 15, 78, 98 }
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
<li>Directory: <code>ES6_data_manipulation</code></li>
<li>File: <code>6-set.js</code></li>
</ul>
</div>

<h3 class="panel-title">
7. More set data structure
</h3>

Create a function named <code>hasValuesFromArray</code> that returns a boolean if all the elements in the array exist within the set.</p>

<p>It accepts two arguments: a <code>set</code> (Set) and an <code>array</code> (Array). </p>

<pre><code>bob@dylan:~$ cat 7-main.js
import hasValuesFromArray from &quot;./7-has_array_values.js&quot;;

console.log(hasValuesFromArray(new Set([1, 2, 3, 4, 5]), [1]));
console.log(hasValuesFromArray(new Set([1, 2, 3, 4, 5]), [10]));
console.log(hasValuesFromArray(new Set([1, 2, 3, 4, 5]), [1, 10]));

bob@dylan:~$
bob@dylan:~$ npm run dev 7-main.js
true
false
false
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
<li>Directory: <code>ES6_data_manipulation</code></li>
<li>File: <code>7-has_array_values.js</code></li>
</ul>
</div>

<h3 class="panel-title">
8. Clean set
</h3>

Create a function named <code>cleanSet</code> that returns a string of all the set values that start with a specific string (<code>startString</code>).</p>

<p>It accepts two arguments: a <code>set</code> (Set) and a <code>startString</code> (String). </p>

<p>When a value starts with <code>startString</code> you only append the rest of the string. The string contains all the values of the set separated by <code>-</code>. </p>

<pre><code>bob@dylan:~$ cat 8-main.js
import cleanSet from &quot;./8-clean_set.js&quot;;

console.log(cleanSet(new Set([&#39;bonjovi&#39;, &#39;bonaparte&#39;, &#39;bonappetit&#39;, &#39;banana&#39;]), &#39;bon&#39;));
console.log(cleanSet(new Set([&#39;bonjovi&#39;, &#39;bonaparte&#39;, &#39;bonappetit&#39;, &#39;banana&#39;]), &#39;&#39;));

bob@dylan:~$
bob@dylan:~$ npm run dev 8-main.js
jovi-aparte-appetit

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
<li>Directory: <code>ES6_data_manipulation</code></li>
<li>File: <code>8-clean_set.js</code></li>
</ul>
</div>

<h3 class="panel-title">
9. Map data structure
</h3>

Create a function named <code>groceriesList</code> that returns a map of groceries with the following items (name, quantity): </p>

<pre><code>Apples, 10
Tomatoes, 10
Pasta, 1
Rice, 1
Banana, 5
</code></pre>

<p>Result:</p>

<pre><code>bob@dylan:~$ cat 9-main.js
import groceriesList from &quot;./9-groceries_list.js&quot;;

console.log(groceriesList());

bob@dylan:~$
bob@dylan:~$ npm run dev 9-main.js
Map {
&#39;Apples&#39; =&gt; 10,
&#39;Tomatoes&#39; =&gt; 10,
&#39;Pasta&#39; =&gt; 1,
&#39;Rice&#39; =&gt; 1,
&#39;Banana&#39; =&gt; 5
}
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
<li>Directory: <code>ES6_data_manipulation</code></li>
<li>File: <code>9-groceries_list.js</code></li>
</ul>
</div>

<h3 class="panel-title">
10. More map data structure
</h3>

Create a function named <code>updateUniqueItems</code> that returns an updated map for all items with initial quantity at 1.</p>

<p>It should accept a map as an argument. The map it accepts for argument is similar to the map you create in the previous task.</p>

<p>For each entry of the map where the quantity is 1, update the quantity to 100.
If updating the quantity is not possible (argument is not a map) the error <code>Cannot process</code> should be thrown.</p>

<pre><code>bob@dylan:~$ cat 10-main.js
import updateUniqueItems from &quot;./10-update_uniq_items.js&quot;;
import groceriesList from &quot;./9-groceries_list.js&quot;;

const map = groceriesList();
console.log(map);

updateUniqueItems(map)
console.log(map);

bob@dylan:~$
bob@dylan:~$ npm run dev 10-main.js
Map {
&#39;Apples&#39; =&gt; 10,
&#39;Tomatoes&#39; =&gt; 10,
&#39;Pasta&#39; =&gt; 1,
&#39;Rice&#39; =&gt; 1,
&#39;Banana&#39; =&gt; 5
}
Map {
&#39;Apples&#39; =&gt; 10,
&#39;Tomatoes&#39; =&gt; 10,
&#39;Pasta&#39; =&gt; 100,
&#39;Rice&#39; =&gt; 100,
&#39;Banana&#39; =&gt; 5
}
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
<li>Directory: <code>ES6_data_manipulation</code></li>
<li>File: <code>10-update_uniq_items.js</code></li>
</ul>
</div>

</details>
