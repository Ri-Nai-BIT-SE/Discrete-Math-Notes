import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "离散数学复习笔记",
  description: "离散数学学习笔记总索引",
  srcDir: "docs",
  base: "/Discrete-Math-Notes/",
  markdown: {
    math: true
  },
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      { text: '首页', link: '/' },
      { 
        text: '数理逻辑',
        items: [
          { text: '命题逻辑', link: '/数理逻辑/命题逻辑/' },
          { text: '一阶谓词逻辑', link: '/数理逻辑/一阶谓词逻辑/' },
          { text: '公式的解释', link: '/数理逻辑/公式的解释/' },
          { text: '形式系统', link: '/数理逻辑/形式系统/' }
        ]
      },
      { 
        text: '集合论',
        items: [
          { text: '集合代数', link: '/集合论/集合代数/' },
          { text: '二元关系的性质', link: '/集合论/二元关系/二元关系的性质/' },
          { text: '关系的闭包', link: '/集合论/二元关系/关系的闭包/' },
          { text: '偏序关系', link: '/集合论/二元关系/偏序关系/' },
          { text: '等价关系', link: '/集合论/二元关系/等价关系/' },
          { text: '函数', link: '/集合论/函数/' }
        ]
      },
      { 
        text: '代数结构',
        items: [
          { text: '代数系统', link: '/代数结构/代数系统/' },
          { text: '群、子群与陪集', link: '/代数结构/群与环/群、子群与陪集/' },
          { text: '循环群与置换群', link: '/代数结构/群与环/循环群与置换群/' },
          { text: '环与域', link: '/代数结构/群与环/环与域/' },
          { text: '格与布尔代数', link: '/代数结构/群与环/格与布尔代数/' }
        ]
      },
      { 
        text: '图论',
        items: [
          { text: '图的基本概念', link: '/图论/图的基本概念/' },
          { text: '扩大路径法', link: '/图论/扩大路径法/' },
          { text: '二部图', link: '/图论/二部图/' },
          { text: '欧拉图与哈密顿图', link: '/图论/欧拉图与哈密顿图/' },
          { text: '树', link: '/图论/树/' },
          { text: '平面图', link: '/图论/平面图/' },
          { text: '着色', link: '/图论/着色/' }
        ]
      }
    ],

    sidebar: {
      '/数理逻辑/': [
        {
          text: '数理逻辑',
          items: [
            { text: '命题逻辑', link: '/数理逻辑/命题逻辑/' },
            { text: '一阶谓词逻辑', link: '/数理逻辑/一阶谓词逻辑/' },
            { text: '公式的解释', link: '/数理逻辑/公式的解释/' },
            { text: '形式系统', link: '/数理逻辑/形式系统/' }
          ]
        }
      ],
      '/集合论/': [
        {
          text: '集合论基础',
          items: [
            { text: '集合代数', link: '/集合论/集合代数/' },
            { text: '函数', link: '/集合论/函数/' }
          ]
        },
        {
          text: '二元关系',
          items: [
            { text: '二元关系的性质', link: '/集合论/二元关系/二元关系的性质/' },
            { text: '关系的闭包', link: '/集合论/二元关系/关系的闭包/' },
            { text: '偏序关系', link: '/集合论/二元关系/偏序关系/' },
            { text: '等价关系', link: '/集合论/二元关系/等价关系/' }
          ]
        }
      ],
      '/代数结构/': [
        {
          text: '代数系统',
          items: [
            { text: '代数系统', link: '/代数结构/代数系统/' }
          ]
        },
        {
          text: '群与环',
          items: [
            { text: '群、子群与陪集', link: '/代数结构/群与环/群、子群与陪集/' },
            { text: '循环群与置换群', link: '/代数结构/群与环/循环群与置换群/' },
            { text: '环与域', link: '/代数结构/群与环/环与域/' },
            { text: '格与布尔代数', link: '/代数结构/群与环/格与布尔代数/' }
          ]
        }
      ],
      '/图论/': [
        {
          text: '图论',
          items: [
            { text: '图的基本概念', link: '/图论/图的基本概念/' },
            { text: '扩大路径法', link: '/图论/扩大路径法/' },
            { text: '二部图', link: '/图论/二部图/' },
            { text: '欧拉图与哈密顿图', link: '/图论/欧拉图与哈密顿图/' },
            { text: '树', link: '/图论/树/' },
            { text: '平面图', link: '/图论/平面图/' },
            { text: '着色', link: '/图论/着色/' }
          ]
        }
      ]
    },

    socialLinks: [
      { icon: 'github', link: 'https://github.com/Ri-Nai-BIT-SE/Discrete-Math-Notes' }
    ],

    footer: {
      message: '离散数学复习笔记',
      copyright: 'Copyright © 2025 Ri-Nai'
    },

    search: {
      provider: 'local'
    }
  }
})
