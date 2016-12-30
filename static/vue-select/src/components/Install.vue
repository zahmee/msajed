<template>
<h2 class="page-header">Install &amp; and Usage</h2>
<p>Install from GitHub via NPM</p>
<pre><code class="language-bash">npm install sagalbot/vue-select</code></pre>

<pre v-pre>
<code class="language-markup">&#x3C;template&#x3E;
  &#x3C;div id=&#x22;myApp&#x22;&#x3E;
    &#x3C;v-select :value.sync=&#x22;selected&#x22; :options=&#x22;options&#x22;&#x3E;&#x3C;/v-select&#x3E;
  &#x3C;/div&#x3E;
&#x3C;/template&#x3E;</code>

<code class="language-markup">&#x3C;script&#x3E;</code>
  <code class="language-javascript">import vSelect from &#x27;vue-select&#x27;
  export default {
    components: {vSelect},

    data() {
      return {
        selected: null,
        options: [&#x27;foo&#x27;,&#x27;bar&#x27;,&#x27;baz&#x27;]
      }
    }
  }</code><code class="language-markup">
&#x3C;/script&#x3E;</code>
</pre>
</template>

<script>
  export default {}
</script>