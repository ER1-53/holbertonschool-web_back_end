# ES6-Promises

<p><img src="https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2019/12/75862d67ca51a042003c.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20240123%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20240123T085247Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=1dc09c327871ed364d66b27b545882a77d20fe61f58df9be66b84758545226ad" alt="" loading='lazy' style="" /></p>

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/aNukpnQLStWa6kqBScmZuA" title="Promise" target="_blank">Promise</a></li>
<li><a href="/rltoken/oE70cO9HPu1lOGuPFzYXXw" title="JavaScript Promise: An introduction" target="_blank">JavaScript Promise: An introduction</a></li>
<li><a href="/rltoken/7IuGsWrFjpvdJkNJ2nVhNg" title="Await" target="_blank">Await</a></li>
<li><a href="/rltoken/dA3jsQCVsvT1tslyo_8HJQ" title="Async" target="_blank">Async</a></li>
<li><a href="/rltoken/J7MhpGC9WLbQXe4Jc5hb8Q" title="Throw / Try" target="_blank">Throw / Try</a></li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/r6SRFxG2oYMlRkvuL9HSmw" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<ul>
<li>Promises (how, why, and what)</li>
<li>How to use the <code>then</code>, <code>resolve</code>, <code>catch</code> methods</li>
<li>How to use every method of the Promise object</li>
<li>Throw / Try</li>
<li>The await operator</li>
<li>How to use an <code>async</code> function</li>
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
<li>Install Babel using: <code>npm install --save-dev babel-jest @babel/core @babel/preset-env @babel/cli</code></li>
<li>Install ESLint using: <code>npm install --save-dev eslint</code></li>
</ul>

<h2>Files</h2>

<h3><code>package.json</code></h3>

<details>
<summary>
Click to show/hide file contents</summary>
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
<summary>
Click to show/hide file contents
</summary>
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

<h3><code>utils.js</code></h3>

<p>Use when you get to tasks requiring <code>uploadPhoto</code> and <code>createUser</code>.
<details>
<summary>
Click to show/hide file contents
</summary>
<pre>
<code>
export function uploadPhoto() {
return Promise.resolve({
status: 200,
body: &#39;photo-profile-1&#39;,
});
}</p>

<p>export function createUser() {
return Promise.resolve({
firstName: &#39;Guillaume&#39;,
lastName: &#39;Salva&#39;,
});
}
</code>
</pre>
</details></p>

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

<h2>Response Data Format</h2>

<p><code>uploadPhoto</code> returns a response with the format</p>

<pre><code>{
status: 200,
body: &#39;photo-profile-1&#39;,
}
</code></pre>

<p><code>createUser</code> returns a response with the format</p>

<pre><code>{
firstName: &#39;Guillaume&#39;,
lastName: &#39;Salva&#39;,
}
</code></pre>


<details>
<summary>Click to see: Tasks</summary>

<h3 class="panel-title">
0. Keep every promise you make and only make promises you can keep
</h3>

Return a Promise using this prototype <code>function getResponseFromAPI()</code></p>

<pre><code>bob@dylan:~$ cat 0-main.js
import getResponseFromAPI from &quot;./0-promise.js&quot;;

const response = getResponseFromAPI();
console.log(response instanceof Promise);

bob@dylan:~$
bob@dylan:~$ npm run dev 0-main.js
true
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
<li>Directory: <code>ES6_promise</code></li>
<li>File: <code>0-promise.js</code></li>
</ul>
</div>

<h3 class="panel-title">
1. Don&#39;t make a promise...if you know you can&#39;t keep it
</h3>

Using the prototype below, return a <code>promise</code>. The parameter is a <code>boolean</code>.</p>

<pre><code>getFullResponseFromAPI(success)
</code></pre>

<p>When the argument is:</p>

<ul>
<li><code>true</code>

<ul>
<li>resolve the promise by passing an object with 2 attributes:

<ul>
<li><code>status</code>: <code>200</code></li>
<li><code>body</code>: <code>&#39;Success&#39;</code></li>
</ul></li>
</ul></li>
<li><code>false</code>

<ul>
<li>reject the promise with an error object with the message <code>The fake API is not working currently</code></li>
</ul></li>
</ul>

<p>Try testing it out for yourself</p>

<pre><code>bob@dylan:~$ cat 1-main.js
import getFullResponseFromAPI from &#39;./1-promise&#39;;

console.log(getFullResponseFromAPI(true));
console.log(getFullResponseFromAPI(false));

bob@dylan:~$
bob@dylan:~$ npm run dev 1-main.js
Promise { { status: 200, body: &#39;Success&#39; } }
Promise {
&lt;rejected&gt; Error: The fake API is not working currently
...
...
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
<li>Directory: <code>ES6_promise</code></li>
<li>File: <code>1-promise.js</code></li>
</ul>
</div>

<h3 class="panel-title">
2. Catch me if you can!
</h3>

Using the function prototype below</p>

<pre><code>function handleResponseFromAPI(promise)
</code></pre>

<p>Append three handlers to the function:</p>

<ul>
<li>When the Promise resolves, return an object with the following attributes

<ul>
<li><code>status</code>: <code>200</code></li>
<li><code>body</code>: <code>success</code></li>
</ul></li>
<li>When the Promise rejects, return an empty <code>Error</code> object</li>
<li>For every resolution, log <code>Got a response from the API</code> to the console</li>
</ul>

<pre><code>bob@dylan:~$ cat 2-main.js
import handleResponseFromAPI from &quot;./2-then&quot;;

const promise = Promise.resolve();
handleResponseFromAPI(promise);

bob@dylan:~$
bob@dylan:~$ npm run dev 2-main.js
Got a response from the API
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
<li>Directory: <code>ES6_promise</code></li>
<li>File: <code>2-then.js</code></li>
</ul>
</div>

<h3 class="panel-title">
3. Handle multiple successful promises
</h3>

In this file, import <code>uploadPhoto</code> and <code>createUser</code> from <code>utils.js</code></p>

<p>Knowing that the functions in <code>utils.js</code> return promises, use the prototype below to collectively resolve all promises and log <code>body firstName lastName</code> to the console.</p>

<pre><code>function handleProfileSignup()
</code></pre>

<p>In the event of an error, log <code>Signup system offline</code> to the console</p>

<pre><code>bob@dylan:~$ cat 3-main.js
import handleProfileSignup from &quot;./3-all&quot;;

handleProfileSignup();

bob@dylan:~$
bob@dylan:~$ npm run dev 3-main.js
photo-profile-1 Guillaume Salva
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
<li>Directory: <code>ES6_promise</code></li>
<li>File: <code>3-all.js</code></li>
</ul>
</div>

<h3 class="panel-title">
4. Simple promise
</h3>

Using the following prototype</p>

<pre><code>function signUpUser(firstName, lastName) {
}
</code></pre>

<p>That returns a resolved promise with this object:</p>

<pre><code>{
firstName: value,
lastName: value,
}
</code></pre>

<pre><code>bob@dylan:~$ cat 4-main.js
import signUpUser from &quot;./4-user-promise&quot;;

console.log(signUpUser(&quot;Bob&quot;, &quot;Dylan&quot;));

bob@dylan:~$
bob@dylan:~$ npm run dev 4-main.js
Promise { { firstName: &#39;Bob&#39;, lastName: &#39;Dylan&#39; } }
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
<li>Directory: <code>ES6_promise</code></li>
<li>File: <code>4-user-promise.js</code></li>
</ul>
</div>

<h3 class="panel-title">
5. Reject the promises
</h3>

Write and export a function named <code>uploadPhoto</code>. It should accept one argument <code>fileName</code> (string). </p>

<p>The function should return a Promise rejecting with an Error and the string <code>$fileName cannot be processed</code></p>

<pre><code>export default function uploadPhoto(filename) {

}
</code></pre>

<pre><code>bob@dylan:~$ cat 5-main.js
import uploadPhoto from &#39;./5-photo-reject&#39;;

console.log(uploadPhoto(&#39;guillaume.jpg&#39;));

bob@dylan:~$
bob@dylan:~$ npm run dev 5-main.js
Promise {
&lt;rejected&gt; Error: guillaume.jpg cannot be processed
..
..
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
<li>Directory: <code>ES6_promise</code></li>
<li>File: <code>5-photo-reject.js</code></li>
</ul>
</div>

<h3 class="panel-title">
6. Handle multiple promises
</h3>

Import <code>signUpUser</code> from <code>4-user-promise.js</code> and <code>uploadPhoto</code> from <code>5-photo-reject.js</code>.</p>

<p>Write and export a function named <code>handleProfileSignup</code>. It should accept three arguments <code>firstName</code> (string), <code>lastName</code> (string), and <code>fileName</code> (string). The function should call the two other functions. When the promises are all settled it should return an array with the following structure:</p>

<pre><code>[
{
status: status_of_the_promise,
value: value or error returned by the Promise
},
...
]
</code></pre>

<pre><code>bob@dylan:~$ cat 6-main.js
import handleProfileSignup from &#39;./6-final-user&#39;;

console.log(handleProfileSignup(&quot;Bob&quot;, &quot;Dylan&quot;, &quot;bob_dylan.jpg&quot;));

bob@dylan:~$
bob@dylan:~$ npm run dev 6-main.js
Promise { &lt;pending&gt; }
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
<li>Directory: <code>ES6_promise</code></li>
<li>File: <code>6-final-user.js</code></li>
</ul>
</div>

<h3 class="panel-title">
7. Load balancer
</h3>

Write and export a function named <code>loadBalancer</code>. It should accept two arguments <code>chinaDownload</code> (Promise) and <code>USDownload</code> (Promise).</p>

<p>The function should return the value returned by the promise that resolved the first.</p>

<pre><code>export default function loadBalancer(chinaDownload, USDownload) {

}
</code></pre>

<pre><code>bob@dylan:~$ cat 7-main.js
import loadBalancer from &quot;./7-load_balancer&quot;;

const ukSuccess = &#39;Downloading from UK is faster&#39;;
const frSuccess = &#39;Downloading from FR is faster&#39;;

const promiseUK = new Promise(function(resolve, reject) {
setTimeout(resolve, 100, ukSuccess);
});

const promiseUKSlow = new Promise(function(resolve, reject) {
setTimeout(resolve, 400, ukSuccess);
});

const promiseFR = new Promise(function(resolve, reject) {
setTimeout(resolve, 200, frSuccess);
});

const test = async () =&gt; {
console.log(await loadBalancer(promiseUK, promiseFR));
console.log(await loadBalancer(promiseUKSlow, promiseFR));
}

test();

bob@dylan:~$
bob@dylan:~$ npm run dev 7-main.js
Downloading from UK is faster
Downloading from FR is faster
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
<li>Directory: <code>ES6_promise</code></li>
<li>File: <code>7-load_balancer.js</code></li>
</ul>
</div>

<h3 class="panel-title">
8. Throw an error
</h3>

Write a function named <code>divideFunction</code> that will accept two arguments: <code>numerator</code> (Number) and <code>denominator</code> (Number).</p>

<p>When the <code>denominator</code> argument is equal to 0, the function should throw a new error with the message <code>cannot divide by 0</code>. Otherwise it should return the numerator divided by the denominator.</p>

<pre><code>export default function divideFunction(numerator, denominator) {

}
</code></pre>

<pre><code>bob@dylan:~$ cat 8-main.js
import divideFunction from &#39;./8-try&#39;;

console.log(divideFunction(10, 2));
console.log(divideFunction(10, 0));

bob@dylan:~$
bob@dylan:~$ npm run dev 8-main.js
5
..../8-try.js:15
throw Error(&#39;cannot divide by 0&#39;);
^
.....

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
<li>Directory: <code>ES6_promise</code></li>
<li>File: <code>8-try.js</code></li>
</ul>
</div>

<h3 class="panel-title">
9. Throw error / try catch
</h3>

Write a function named <code>guardrail</code> that will accept one argument <code>mathFunction</code> (Function).</p>

<p>This function should create and return an array named <code>queue</code>. </p>

<p>When the <code>mathFunction</code> function is executed, the value returned by the function should be appended to the queue.
If this function throws an error, the error message should be appended to the queue.
In every case, the message <code>Guardrail was processed</code> should be added to the queue. </p>

<p>Example:</p>

<pre><code>[
1000,
&#39;Guardrail was processed&#39;,
]
</code></pre>

<pre><code>bob@dylan:~$ cat 9-main.js
import guardrail from &#39;./9-try&#39;;
import divideFunction from &#39;./8-try&#39;;

console.log(guardrail(() =&gt; { return divideFunction(10, 2)}));
console.log(guardrail(() =&gt; { return divideFunction(10, 0)}));

bob@dylan:~$
bob@dylan:~$ npm run dev 9-main.js
[ 5, &#39;Guardrail was processed&#39; ]
[ &#39;Error: cannot divide by 0&#39;, &#39;Guardrail was processed&#39; ]
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
<li>Directory: <code>ES6_promise</code></li>
<li>File: <code>9-try.js</code></li>
</ul>
</div>

</details>
