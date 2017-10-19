<template>
    <div id="app">
        <router-view></router-view>
        <!--<div>-->
            <!--selected id:{{selected}}-->
        <!--</div>-->


        <mt-tabbar fixed v-model="selected" @click.native="changeRoute">
            <mt-tab-item id="1">
                <img slot="icon" src="./assets/home.png">
                主页
            </mt-tab-item>
            <mt-tab-item id="2">
                <img slot="icon" src="./assets/classify.png">
                发现
            </mt-tab-item>
            <mt-tab-item id="3">
                <img slot="icon" src="./assets/my.png">
                我的
            </mt-tab-item>
        </mt-tabbar>

    </div>

</template>

<script>
    import axios from 'axios'
    import router from './router'
    import {mapMutations, mapState, mapActions} from 'vuex'
    export default {

        name: 'app',
        computed: {
            ...mapState([
                // 映射 this.count 为 store.state.count
                'info_api',
                'log_in'
            ])
        },
        data () {
            return {
                msg: 'Welcome to Your Vue.js App',
                myData: '',
                selected: ''
            }
        },
        methods: {
            changeRoute () {
                if (this.selected == 1)
                    router.push('home');
                else if (this.selected == 2)
                    router.push('class');
                else if (this.selected == 3)
                    router.push('my');
            },
            get () {
                axios.get('a.txt').then(function (res) {
                    console.log(res.data)
                }).catch(function (err) {
                    console.log('Failed' + err)
                })
            },
            ...mapMutations([
                'changeLogin',
                'setInfo'
            ]),
            ...mapActions([
                'decrement'
            ])
        },
        created () {
            console.log('created func called')
            if (this.log_in == false) {
                let self = this
                axios.get(this.info_api).then(function (res) {
                    self.changeLogin()  //提交登录状态的改变
                    var i = res.data['info']
//                    console.log(i)
                    self.setInfo(i)  // 将从api获取到的sInfo赋给vuex中的state
                    // 后退一步记录，等同于 history.back()
//                    router.go(-1)
                }).catch(function (error) {
                    console.log('初始化登录失败')
//                    console.log(error.response.data['msg']);
                })

            }
        }
    }
</script>

<style>
    #app {
        font-family: 'Avenir', Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: #2c3e50;
        margin-top: 60px;
    }

    h1, h2 {
        font-weight: normal;
    }

    ul {
        list-style-type: none;
        padding: 0;
    }

    li {
        display: inline-block;
        margin: 0 10px;
    }

    a {
        color: #42b983;
    }
</style>
