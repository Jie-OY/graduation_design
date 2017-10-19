import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

var state = {
    info: {},   // 换为undefined会报错 info.sName undefined
    log_in: false,
    login_api: '/login',
    info_api: '/info',
    quiz_list_api: '/quiz/list',    // 获取课程和章节列表
    quiz_items_api: '/quiz/items',  // 获取当前测试所有题目
    quiz_check_api: '/quiz/check',
    // selected: ''     //tabbar id
};

const mutations = {
    setInfo (state, new_info) {
        state.info = new_info
    },
    changeLogin (state) {
        state.log_in = true
    },
    decrement (state) {
        state.count--
    },
    // getToken(state, new_token){
    //     state.token = new_token
    // }
};

const actions = {
    increment ({commit}) {
        commit('increment')
    },
    decrement ({commit}) {
        commit('decrement')
    },
    clickAsync ({commit, state}) {

    }

};
// 与上面是等同的，上面用到了ES6的参数解析，commit相当于取context（一个store对象）的commit属性的value（commit:commit的缩写）
const actions2 = {
    increment (context) {
        context.commit('increment')
    }
};

var vuex = new Vuex.Store({
    state,
    mutations,
    actions
})

export default vuex