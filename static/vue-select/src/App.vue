<style lang="scss">

  @import 'variables.scss';

  body {
    color: #404040;
  }

  .jumbotron-top {
    color: $black;
    background: $blue;
    background: linear-gradient(to top, rgba(76,195,217,1) 0%,rgba(152,227,234,1) 100%);
    // background: linear-gradient(45deg, rgba(76,195,217,1) 0%,rgba(152,227,234,1) 100%);
    margin-bottom: 0;
  }

  .jumbotron.jumbotron-green {
    padding: 75px 0;
  }

  #v-select .dropdown-toggle {
    background: #fff;
  }

  /* Cyan theme */
  #v-select .selected-tag {
    color: #147688;
    background-color: #d7f3f9;
    border-color: #91ddec;
  }

  #v-select.dropdown.open .dropdown-toggle,
  #v-select.dropdown.open .dropdown-menu {
    border-color: #4CC3D9;
  }

  #v-select .active a {
    background: rgba(50,50,50,.1);
    color: #333;
  }

  #v-select.dropdown .highlight a,
  #v-select.dropdown li:hover a {
    background: #4CC3D9;
    color: #fff;
  }
</style>

<template>
  <div class="jumbotron jumbotron-top">
    <div class="container">
      <div class="col-md-8 col-md-offset-2">
      <h1>Vue Select</h1>
        <p class="lead">A well-tested Vue.js component that provides similar functionality to Select2/Chosen without the overhead of jQuery.</p>
        <!-- <p>Vue-select has no JavaScript dependencies</p> -->
        <ul class="unstyled lead">
          <li>No JS dependencies</li>
          <li>Works with Vuex</li>
          <li>Reactive <small>(as you'd expect from a Vue component)</small></li>
        </ul>

        <a class="btn btn-primary" href="https://github.com/sagalbot/vue-select"><span class="octicon octicon-mark-github"></span> View on GitHub</a>
      </div>
    </div>
  </div>

  <jumbotron></jumbotron>

  <div class="container">
    <div class="col-md-10 col-md-offset-1">
      <install></install>
      <params></params>
    </div>
  </div>
</template>

<script>
import Jumbotron from './components/Jumbotron.vue'
import Install from './components/Install.vue'
import Params from './components/Params.vue'

export default {
  components: { Jumbotron, Params, Install },
}
</script>
