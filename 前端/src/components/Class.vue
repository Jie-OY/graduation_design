<template>
    <div>
        <mt-navbar fixed v-model="selected">
            <mt-tab-item id="1">在线练习</mt-tab-item>
            <mt-tab-item id="2">成绩查询</mt-tab-item>
            <mt-tab-item id="3">意见反馈</mt-tab-item>
            <!--<mt-tab-item id="4" icon="../assets/my.png">&or;</mt-tab-item>-->
        </mt-navbar>

        <!-- tab-container -->
        <mt-tab-container v-model="selected">
            <mt-tab-container-item id="1">
                <Class_quiz></Class_quiz>
            </mt-tab-container-item>
            <mt-tab-container-item id="2">
                <Class_query></Class_query>
            </mt-tab-container-item>
            <mt-tab-container-item id="3">
                <Class_advice></Class_advice>
            </mt-tab-container-item>

        </mt-tab-container>
        <br>
    </div>
</template>

<script>
    import Class_quiz from './Class_quiz.vue'
    import Class_query from './Class_query.vue'
    import Class_advice from './Class_advice.vue'
    import {TabContainer, TabContainerItem} from 'mint-ui';
    import {Navbar, TabItem} from 'mint-ui';
    import router from '../router'
    export default{
        name: 'Class',
        components: {
            // 将myComponent组件注册到Vue实例下
            'Class_quiz' : Class_quiz,
            'Class_query' : Class_query,
            'Class_advice' : Class_advice,
        },
        data () {
            return {
                active: "tab-container1",
                selected: '1'       // 必须是 '1'，不能是 1.
            }
        },
//        watch: {
//            selected: function (val, oldVal) {
//                console.log('selected: '+this.selected)
//                console.log('new value: '+val)
//
//                if (val == 1) {
//                    router.replace('class/quiz');
//                }    // 在线测试
//                else if (val == 2) {
//                    router.replace('class/query')
//                }   // 成绩查询
//                else {
//                    router.replace('class/advice')
//                }    // 待定为意见反馈
//            }
//        },
    }
</script>

<style></style>