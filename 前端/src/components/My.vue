<template>
    <div>

        <mt-header :title="state?'我的资料':'编辑资料'" fixed>
            <mt-button v-if="log_in && !state" icon="back" slot="left" @click.native="cancel">取消</mt-button>
            <mt-button v-if="log_in==true" icon="" slot="right" @click.native="editInfo">{{state?'编辑':'完成'}}</mt-button>
        </mt-header>

        <!--log_state = false-->

        <mt-cell v-if="log_in==false" title="登录" value="请先登录" is-link style="text-align: left" to="/login">
            <img slot="icon" src="../assets/my.png" width="24" height="24">
        </mt-cell>

        <!--log_state = true-->
        <div v-if="log_in==true">
            <mt-field eld label="用户名" placeholder="请输入用户名" v-model="info.UserICode" :readonly="state"
                      :disableClear="state"></mt-field>
            <mt-field label="密码" placeholder="请输入密码" :type="show_pwd?'':'password'" v-model="info.UserIPsd"
                      :readonly="state"
                      :disableClear="state">
                <mt-switch style="margin-top: 8px" v-model="show_pwd"></mt-switch>
            </mt-field>
            <mt-field label="姓名" placeholder="请输入姓名" v-model="info.Name" :readonly="state"
                      :disableClear="state"></mt-field>
            <mt-field eld label="学号" placeholder="请输入学号" v-model="info.UserIStudentNumber" :readonly="state"
                      :disableClear="state"></mt-field>
            <!--<mt-field label="手机号" placeholder="请输入手机号" type="tel" v-model="info.pNum" :readonly="state"-->
            <!--:disableClear="state"></mt-field>-->
            <mt-field label="性别" placeholder="请输入性别" v-model="info.UserISex" :readonly="state"
                      :disableClear="state"></mt-field>
            <!--<mt-field label="学院" placeholder="请输入学院" v-model="info.institute" :readonly="state"-->
            <!--:disableClear="state"></mt-field>-->
            <!--<mt-field label="班级" placeholder="请输入班级" v-model="info.sClass" :readonly="state"-->
            <!--:disableClear="state"></mt-field>-->
        </div>

    </div>
</template>
<script>
    import {Indicator, Cell, Toast, MessageBox, Switch} from 'mint-ui';
    import {mapState, mapMutations, mapActions} from 'vuex'
    import router from '../router';
    import axios from 'axios'
    export default{
        name: 'my',
        computed: {
            ...mapState([
                'info',
                'log_in'
            ])
        },
        data () {
            return {
                state: true,    // true为展示状态，false为修改状态
                show_pwd: false,    // 通过绑定type属性，标志密码是否要明文显示
                chInfoUrl: '/info',
                loading: false,
                info_c: {
                    // columns = ['ID', 'Name', 'pNum', 'UserIPsd', 'UserISex', 'institute', 'sClass','UserIStudentNumber' ]
                }
            }
        },
        methods: {
            ...mapMutations([
                'setInfo',  //从后端获取学生的信息
            ]),
            editInfo () {
                if (this.state) {
                    this.state = !this.state;
                    console.log(this.info)
                    this.info_c = JSON.parse(JSON.stringify(this.info))
                }
                else {
                    this.commitEdit()
                    this.state = !this.state;

                }
            },
            cancel () {
                this.state = !this.state;
                this.setInfo(this.info_c)
//                this.info = JSON.parse(JSON.stringify(this.info_c));

            },
            commitEdit () {
                this.show_pwd = false
                var self = this;    //  be   careful   !!!
                Indicator.open({
                    text: '修改中...',
                    spinnerType: 'snake'
                })      // 在本地测试的时候，由于ajax请求完成的还是比较快的，所以看不到
//                console.log(self.chInfoUrl+self.info.sNum   ) 将修改信息的url和学号拼接起来
                axios.put(self.chInfoUrl, self.info).then(function (res) {
                    Indicator.close()
//                        self.info = res.data
                    Toast({
                        message: '修改成功',
                        iconClass: 'icon icon-success',
                        duration: 1500
                    });
                    self.setInfo(res.data['info'])
                }).catch(function (err) {
                    Indicator.close()
                    MessageBox('提示', err.response.data['errmsg']);
                })
            }
        },
        mounted () {
//            Indicator.open()
        },
        created () {
            if (this.log_in == false) {
//                this.fetchData();
            }

        },
    }
</script>

<style></style>