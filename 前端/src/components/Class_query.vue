<template>
    <div>
        <!--未选择完毕，显示的界面-->
        <div v-if="ready==false">
            <div>
                <mt-cell title="课程选择" style="text-align: left;margin-top: 30px" is-link
                         @click.native="popupVisible1 = true"
                         :value="course_name"></mt-cell>
            </div>

            <div>
                <mt-cell title="章节选择" style="text-align: left;margin-top: 30px" is-link
                         @click.native="popupVisible2 = true"
                         :value="chapter_name"></mt-cell>
            </div>

            <!--开始测验按钮-->
            <div style="text-align: center;margin-top: 50px">
                <mt-button type="primary" size="normal" @click="startQuiz">开始测验</mt-button>
            </div>
        </div>

        <!--选择完毕，测试界面-->
        <div v-else>
            <mt-field label="" placeholder="自我介绍" type="textarea" rows="4" v-model="item[2]"
                      readonly="'true'"></mt-field>
            <div>
                <!--填空、问答显示界面-->
                <div v-if="item_type=='问答题'||item_type=='填空题'">
                    <mt-field label="回答" placeholder="填空题请以空白字符隔开答案" type="textarea" rows="4"
                              v-model="item_answer"></mt-field>
                </div>
                <!--判断题显示界面-->
                <div v-else-if="item_type=='判断题'">
                    <mt-radio
                            title=""
                            v-model="item_answer"
                            :options="['T', 'F']">
                    </mt-radio>
                </div>
                <!--选择题显示界面-->
                <div v-else>
                    <mt-checklist
                            title="fd"
                            v-model="item_answer"
                            :options="options">
                    </mt-checklist>
                </div>
            </div>

            <div>
                <!--下一题按钮-->
                <mt-button type="primary" size="large" @click="nextItem">{{end_flag?'提交':'下一题'}}</mt-button>
            </div>
        </div>
        <mt-checklist
                title="fd"
                v-model="tmp"
                :options="options">
        </mt-checklist>
        <!--POPUP课程选择组件-->
        <mt-popup v-model="popupVisible1" position="bottom" style="width: 100%">
            <mt-picker :slots="courseSlots" @change="onCourseChange" :visible-item-count="5"
                       :show-toolbar="false"></mt-picker>
            &nbsp;
            <mt-button style="margin-bottom: 1px" size="large" type="primary" @click.native="popupVisible1 = false">
                确定
            </mt-button>
        </mt-popup>

        <!--POPUP章节选择组件-->
        <mt-popup v-model="popupVisible2" position="bottom" style="width: 100%">
            <mt-picker :slots="chapterSlots" @change="onChapterChange" :visible-item-count="5"
                       :show-toolbar="false"></mt-picker>
            &nbsp;
            <mt-button style="margin-bottom: 1px" size="large" type="primary" @click.native="popupVisible2 = false">
                确定
            </mt-button>
        </mt-popup>
    </div>
    {{course_name}}
</template>

<script>
    import {Picker, Indicator, MessageBox, Field, Radio, Checklist, Button} from 'mint-ui'
    import axios from 'axios'
    import {mapState} from 'vuex'

    export default{
        computed: {
            ...mapState([
                'quiz_list_api',
                'quiz_items_api',
                'quiz_check_api',
            ]),
            item_type: function () {
                return this.item[1]
            },
            item: function () {
                return this.items[this.item_index]

            },
            choices_item: function () {
                console.log('选择题选项数据：')
                console.log(this.item.slice(3))
                return this.item.slice(3)

            },
            item_count: function () {
                return this.items.length

            },
            // 标识当前题目是否为最后一道题
            end_flag: function () {
                return this.item_count == (this.item_index + 1)

            }
        },
        data(){
            return {
                tmp:[],
                ready: false,       // 是否一切选择完毕，可以进入到测试页面
                course_chapter_dict: {},
                item_index: 0,
                // Type:选择题为数组（即使单选），填空和问答是String，判断是String
                item_answer: undefined,
                items: [],      // 题库
                answers: [],
//                item: [],       // 单道题
                course_name: '',
                chapter_name: '',
                popupVisible1: false,       // 课程选择器是否可见
                popupVisible2: false,       // 章节选择器是否可见
                courseSlots: [{
                    flex: 1,
                    values: [],
                    className: 'slot1'
                }],
                chapterSlots: [{
                    flex: 1,
                    values: ['第一章 概述', '第二章 80x86微处理器', '第三章 80x86指令系统', '实验四 8255并行口实验：控制交通灯实验', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995'],
                    className: 'slot1'
                }],
            }
        },
        watch: {
            // 在课程发生变化时，章节也发生相应变化
            course_name: function (val, oldVal) {
                this.chapterSlots[0].values = this.course_chapter_dict[val]
            },
            item_index: function (val, oldVal) {

            },
        },
        methods: {
            // 这里两个参数的含义
            onCourseChange(picker, values) {
                this.course_name = values[0];
            },
            onChapterChange(picker, values) {
                this.chapter_name = values[0];
            },
            startQuiz(){
                Indicator.open({
                    text: 'Waiting',
                    spinnerType: 'snake'
                })
                let self = this
                axios.get(this.quiz_items_api + '/' + this.chapter_name).then(function (res) {
                    Indicator.close()
                    self.items = res.data['items']
                    self.ready = true
                }).catch(function (err) {
                    Indicator.close()
                    MessageBox('提示', err.response.data['errmsg']);
                    console.log('获取测验题目失败')
                })
            },
            nextItem (){

                let answer = new Array(this.item[0], this.item_answer)
                this.answers.push(answer)
                if (this.end_flag == true) {
                    Indicator.open({
                        text: '提交中...',
                        spinnerType: 'snake'
                    })
                    axios.post(this.quiz_check_api, {answers: this.answers}).then(function (res) {
                        Indicator.close()
                        MessageBox('提示', res.data['score']);
                    }).catch(function (err) {
                        Indicator.close()
                        MessageBox('提示', err.response.data['errmsg']);
                    })
                }
                console.log('上一题答案')
                console.log(this.item_answer)
                this.item_answer = undefined
                this.item_index++;
                console.log('当前item')
                console.log(this.item)
            }

        },
        created () {
            this.options = [1, 2, 3]

            console.log('获取课程列表...');
            var self = this;
            axios.get(this.quiz_list_api).then(function (res) {
                var list = res.data['course_list'];
                self.courseSlots[0].values = list;
                self.course_chapter_dict = res.data['course_chapter_dict'];
                console.log("获取课程列表完毕")
            }).catch(function (err) {
                console.log("获取课程列表失败")
            })
        }
    }
</script>
