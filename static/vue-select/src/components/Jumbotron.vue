<template>
  <div class="jumbotron">
      <div class="flex-container">
        <div transition="slide-right" v-show="selected" class="flex code">
          <pre>{{ selected | json }}</pre>
        </div>

        <div class="flex center">
          <v-select
            id="v-select"
            :placeholder="placeholder"
            :value="selected"
            :options="options"
            :multiple="multiple"
            :on-change="setSelected"
            >
          </v-select>
        </div>

        <div class="flex code">
            <div>
              <pre class="fake">
                /**<br>
                 * @prop multiple <br>
                 * @type {Boolean} <br>
                 */
              </pre>
              <a @click="toggleMultiple" class="btn btn-code" :class="{ active: multiple }">Multiple</a>
            </div>

            <div>
              <pre class="fake">
                /**<br>
                 * @prop options <br>
                 * @type {Array} <br>
                 */
              </pre>
              <a @click="toggleOptionType" class="btn btn-code">
                <span :class="{active: type === 'advanced'}">[{label:'foo'}]</span> <span class="grey">||</span> <span :class="{active: type === 'simple'}">['foo']</span>
              </a>
            </div>

            <div>
              <pre class="fake">
                /**<br>
                 * @prop placeholder <br>
                 * @type {String} <br>
                 */
              </pre>
              <input @keyup="onPlaceholderChange" type="text" class="btn btn-code" value="{{ placeholder }}">
            </div>
          </div>
      </div>
  </div>
</template>

<script>
  import vSelect from './Select.vue'
  import { setSelected, toggleMultiple, setPlaceholder, toggleOptionType } from '../vuex/actions'

  export default {
    components: { vSelect },
    vuex: {
      getters: {
        placeholder (store) {
          return store.placeholder
        },
        selected (store) {
          return store.selected
        },
        type (store) {
          return store.optionType
        },
        options (store) {
          return store.options[store.optionType]
        },
        multiple (store) {
          return store.multiple
        }
      },
      actions: { setSelected, toggleMultiple, setPlaceholder, toggleOptionType }
    },
    methods: {
      onPlaceholderChange ( e ) {
        this.setPlaceholder( e.target.value )
      }
    }
  }
</script>

<style scoped lang="sass">
  @import '../variables';

  .slide-right-transition {
    opacity: 1;
    transition: all .5s;
  }

  .slide-right-enter, .slide-right-leave {
    opacity: 0;
  }

  .jumbotron {
    padding: 0;
    background: rgba($green, .1);
  }

  .grey {
    color: $code-grey;
  }

  .flex-container {
    padding: 0;
    display: flex;
    align-items: center;
    flex-direction: row;
    justify-content: center;
  }

  .flex {
    display:flex;
    align-self: stretch;
    padding: 0 34px;
  }

  .flex.code:first-child {
    width: 250px;
    color: $code-white;
    align-items: center;
    // flex-grow: 1;
  }

  .flex.center {
    width: 100%;
    align-self: center;
    text-align: center;

    #v-select {
      width: 70%;
      margin: 0 auto;
    }
  }

  .flex.code:last-child {
    // flex-grow: 1;
    width: 280px;
    flex-direction: column;
  }

  .code {
    background: $code-black;
    // color: $code-white;
    text-shadow: 0 1px rgba(0, 0, 0, 0.3);
    font-family: Consolas, Monaco, 'Andale Mono', 'Ubuntu Mono', monospace;
    text-align: left;
    padding: 48px 15px;

    .active {
      color: $code-green;
    }
  }

  .btn-code {
    display: inline-block;
    float: left;
    clear: both;
    margin-bottom: 7px;
    border: 1px solid $code-white;
    color: $code-white;
    box-shadow: none;
    background: none;
    text-shadow: 0 1px rgba(0, 0, 0, 0.3);

    &:focus,
    &:active,
    &:hover,
    &.active {
      color: $code-green;
      border: 1px solid $code-green;
      outline: none;
      box-shadow: none;
      appearance: none;

      .active {
        color: $code-grey;
      }
    }
  }

  .btn-code + pre {
    margin-top: 15px;
  }

  input.btn-code {
    text-align: left;

  }

  pre {
    background: none;
    border: none;
    color: $code-white;
  }

  pre.fake {
    padding: 0;
    white-space: normal;
    border: none;
    background: $code-black;
    color: $code-grey;
  }
</style>