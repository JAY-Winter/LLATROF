import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

const API_URL = 'http://127.0.0.1:8000'

export default new Vuex.Store({
  state: {
    cartegory: [
      {
        title: '청바지',
        imgUrl: 'https://cafe24img.poxo.com/topping99/web/product/big/202104/cd7a0bae031a4e6f570c7244d9eaf3c6.jpg'
      },
      {
        title: '면바지',
        imgUrl: 'http://ssecondedition.com/web/product/big/202009/35f172b9687139f9518105d822b869e1.jpg'
      },
      {
        title: '스웨트',
        imgUrl: 'https://image.msscdn.net/images/goods_img/20190131/945657/945657_2_500.jpg'
      },
      {
        title: '반바지',
        imgUrl: 'https://t1.daumcdn.net/cfile/tistory/245ECF4D555931423A'
      },
      {
        title: '무슨바지',
        imgUrl: 'https://cdn.011st.com/11dims/resize/600x600/quality/75/11src/pd/v2/4/3/5/7/6/9/ZyliI/1585435769_B.jpg'
      },
      {
        title: '나팔바지',
        imgUrl: 'https://contents.lotteon.com/itemimage/LO/13/55/14/19/75/_1/35/51/41/97/6/LO1355141975_1355141976_1.jpg/dims/resizef/720X720'
      },
    ],
    articles: [],
  },
  // 게터, 뮤테이션, 액션은 향후 모듈을 세분화 해도 
  // 이름 그대로 사용가능하니 일단은 분리하지 않고 진행
  getters: {
  },
  mutations: {
    GET_ARTICLES(state, articles) {
      state.articles = articles
    }
  },
  actions: {
    getArticles(context) {
      axios({
        method: 'get',
        url: `${API_URL}/articles/api/articles_list/`
      })
        .then((res) => {
          context.commit('GET_ARTICLES', res.data)
        })
        .catch((error) => console.log(error))
    }
  },
  modules: {
  }
})