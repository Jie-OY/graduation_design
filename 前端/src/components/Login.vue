<template>
    <div>
        <mt-header fixed title="登录">
            <mt-button icon="back" slot="left" @click.native="goBack">返回</mt-button>
        </mt-header>

        <div>
            <!--state = error, success, warning-->
            <mt-field label="用户名" placeholder="请输入用户名" v-model="UserICode"></mt-field>
            <mt-field label="密码" placeholder="请输入密码" type="password" v-model="UserIPsd">

            </mt-field>

            <br>
            <mt-button type="primary" size="large" @click.native="login">登录</mt-button>
        </div>
        <br>
    </div>
</template>

<script>
    import axios from 'axios'
    import router from '../router'
    import {Field, Header, Indicator, MessageBox} from 'mint-ui'
    import {mapState, mapMutations} from 'vuex'
    export default{
        computed: {
            ...mapState([
                'login_api'
            ])
        },
        data () {
            return {
                UserICode: '',
                UserIPsd: '',
//                login_api: '/login',
                failedMsg: '',
            }
        },
        methods: {
            ...mapMutations([
                'changeLogin',
                'setInfo'
            ]),
            goBack () {
//                router.push('home')
                router.go(-1)
            },
            login () {
                var self = this
                Indicator.open({
                    text: '登录中...',
                    spinnerType: 'snake'
                })

                axios.post(this.login_api, {UserICode: this.UserICode, UserIPsd: this.UserIPsd}).then(function (res) {

                    Indicator.close()

                    self.changeLogin()  //提交登录状态的改变
//                    var t = res.data['access_token']
                    var i = res.data['info']
                    self.setInfo(i)  // 将从api获取到的sInfo赋给vuex中的state
                    // 后退一步记录，等同于 history.back()
//                    router.go(-1)
                    router.push('my')
                }).catch(function (error) {
//                    console.log(error.response.data['msg']);
                    Indicator.close()
                    self.pwd = ''
                    MessageBox('提示', error.response.data['errmsg']);
                })
            }
        }
    }
</script>

<style scoped>

</style>