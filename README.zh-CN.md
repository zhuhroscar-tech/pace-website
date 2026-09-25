# Pace Website

[![English](https://img.shields.io/badge/English-555555?style=flat)](README.md) [![简体中文](https://img.shields.io/badge/简体中文-555555?style=flat)](README.zh-CN.md)

Pace 面向大学生的学习辅助项目宣传网站。本仓库包含网站页面和首页演示，**不是完整的 Pace 应用**，也不是医疗工具或可直接上线的报名后端。

![Pace 首页](docs/images/example-output.png)

## 本地预览

需要现代浏览器和 Python 3；Python 用于预览服务器及可选的页面生成。无需 npm 依赖或框架构建。

```bash
git clone https://github.com/zhuhroscar-tech/pace-website.git
cd pace-website
python3 -m http.server 8000 --bind 127.0.0.1
```

打开 `http://127.0.0.1:8000`。仓库中已提交的 HTML 可以直接提供服务，只有修改生成脚本内容或共享片段后才需要重新生成。

## 仓库内容

- 含交互式学习场景示意和产品介绍入口的首页。
- 关于、定价、FAQ、候补名单及四个功能介绍页面。
- 共享导航、移动端菜单、FAQ 折叠面板及滚动显现效果。
- 原生 HTML/CSS/JavaScript，以及生成次级页面的 Python 辅助脚本。

候补名单页面目前提供的是**邮件链接**，并明确提示内嵌报名表尚未上线。仓库中没有可配置后即投入使用的表单后端。Pro 功能属于产品规划，不代表这里已经实现了对应应用能力。

## 应该修改哪些文件

| 修改内容 | 源文件 |
| --- | --- |
| 首页文案与内容 | `index.html`，手工维护 |
| 共享页头与页脚 | `src/partials/` |
| 关于、定价、FAQ、候补名单文案 | `build_pages.py` |
| 功能页文案 | `build_features.py` |
| 样式及浏览器交互 | `assets/css/`、`assets/js/site.js` |

修改生成源或共享片段后运行：

```bash
python3 build_features.py
python3 build_pages.py
```

提交前检查生成的 HTML。这些命令不会重新生成手写首页，因此首页导航的一致性需单独维护。接入真实报名表时，应替换 `build_pages.py` 中的待上线提示块再生成页面，不要依赖仓库之外的本地说明文件。

## 部署与检查

任意静态托管服务均可提供仓库根目录。GitHub Pages 可选择 **Deploy from a branch → main → /(root)**。配置后地址为 `https://<username>.github.io/pace-website/`；本文不假定 Pages 已启用。

发布前检查移动端导航、内部链接、首页演示、FAQ 键盘交互及候补名单邮件链接。Google Fonts 从外部加载。请保留医疗免责声明，并明确区分规划中的功能和已实现的行为。

发布说明维护在 [CHANGELOG.md](CHANGELOG.md)。已发布的源码快照见 [GitHub Releases](https://github.com/zhuhroscar-tech/pace-website/releases)。

提交前运行仓库契约检查：

```bash
python3 build_features.py
python3 build_pages.py
python3 -m unittest discover -s tests -v
```

GitHub Actions 会运行同样的生成器与测试检查，并在生成后的 HTML 未提交时失败。

## 许可证

MIT License。见 [LICENSE](LICENSE)。
