import hashlib
from datetime import datetime
from flask import Blueprint, render_template, request, redirect, url_for,session
from App.models import *


blue = Blueprint('blog', __name__)

#************************************
#登录页面
@blue.route('/admin/login/')
def admin_login():
    return render_template("admin/login.html")


#登录进入主页
@blue.route('/admin/index/',methods=['GET','POST'])
def admin_index():
    
    if request.method == 'POST':
        # 客户端数据传送
        uname = request.form.get('username')
        pwd = request.form.get('userpwd')
        
        admin_user=Admin.query.get(1)
        if admin_user.username == uname and admin_user.userpwd == pwd:

            session['uname'] = uname
            
            return render_template("admin/index.html")
        else:
            return render_template("admin/login.html")
            
    return render_template("admin/index.html")


#返回主页
@blue.route('/admin/bindex/')
def back_index():
    return render_template("admin/index.html")
    
    
#退出
@blue.route('/admin/logout/')
def admin_logout():
    return render_template("admin/login.html")


# ************************************
# 栏目主页
@blue.route('/admin/ranscategory/')
def rans_category():
    categorys = Category.query.filter(Category.id)
    # print(categorys,type(categorys))#查询集
    return render_template('admin/category.html/', categorys=categorys)


# 添加栏目
@blue.route('/admin/addcategory/', methods=["GET", "POST"])
def add_category():
    if request.method == 'POST':
        category = Category()
        category.catename = request.form.get('name')
        category.as_name = request.form.get('alias')
        category.key_word = request.form.get('keywords')
        category.descri = request.form.get('describe')
        
        try:
            db.session.add(category)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            db.session.frush()
            return 'fail:%s' % e
    
    return render_template('admin/category.html/')


# 更新栏目主页
@blue.route('/admin/updatecategory/')
def update_category():
    categorys = Category.query.filter(Category.id)
    return render_template('admin/update-category.html/',categorys=categorys)


# 更新栏目
@blue.route('/admin/updatewritecategory/<int:id>', methods=["GET", "POST"])
def update_write_category(id):
    if request.method == 'POST':
        category = Category.query.filter_by(id=id).first()
        category.catename = request.form.get('name')
        category.as_name = request.form.get('alias')
        category.key_word = request.form.get('keywords')
        category.descri = request.form.get('describe')
    
        db.session.commit()
    categorys = Category.query.filter(Category.id)
    return render_template('admin/category.html',categorys=categorys)

#删除栏目
@blue.route('/admin/delcategory/<int:id>/')
def del_category(id):
    
    category= Category.query.filter_by(id=id).first()
    db.session.delete(category)
    
    db.session.commit()
    return redirect(url_for('blog.rans_category'))

#************************************
#文章主页
@blue.route('/admin/article/')
def art():
    arts = ArtMoel.query.filter(ArtMoel.id)
    return render_template('admin/article.html/',arts=arts)


#增加文章主页
@blue.route('/admin/addarticle/')
def add_art():
    art = ArtMoel.query.filter(ArtMoel.id).first()
    return render_template('admin/add-article.html/',art=art)


# 撰写文章
@blue.route('/admin/writearticle/', methods=["GET", "POST"])
def write_art():
    if request.method == "POST":
        art = ArtMoel()
        art.title = request.form.get('title')
        art.content = request.form.get('content')
        art.keywords = request.form.get('keywords')
        art.describe = request.form.get('describe')
        art.tags = request.form.get('tags')
        art.date = datetime.now()
        art.category =request.form.get("category")
        db.session.add(art)
        db.session.commit()
        
    return redirect(url_for('blog.art'))


#修改文章主页
@blue.route('/admin/updatearticle/<int:id>/')
def update_art(id):
    arts = ArtMoel.query.filter_by(id=id)
    return render_template('admin/update-article.html/',arts=arts)


#修改文章
@blue.route('/admin/fixarticle/',methods=["GET", "POST"])
def fix_art():
    if request.method == "POST":
        id = request.form.get('visibility')
        art = ArtMoel.query.filter_by(id=id).first()
        art.title = request.form.get('title')
        art.content = request.form.get('content')
        art.keywords = request.form.get('keywords')
        art.describe = request.form.get('describe')
        art.tags = request.form.get('tags')
        art.date = datetime.now()
        db.session.commit()
    arts = ArtMoel.query.filter(ArtMoel.id)
    return render_template('admin/article.html/', arts=arts)

#删除文章
@blue.route('/admin/delarticle/<int:id>/')
def del_art(id):
    art=ArtMoel.query.filter_by(id=id).first()
    
    db.session.delete(art)
    db.session.commit()
    return redirect(url_for('blog.art'))

#************************************
#公告主页
@blue.route('/admin/ransnotice/')
def rans_notice():
    return render_template('admin/notice.html/')


# 增加公告主页
@blue.route('/admin/addnotice/')
def add_notice():
    return render_template('admin/add-notice.html/')


# 撰写公告
# @blue.route('/admin/writenotice/')
# def write_notice():
#     return render_template('admin/add-notice.html/')


#************************************
# 评论主页
@blue.route('/admin/ranscomment/')
def rans_comment():
    return render_template('admin/comment.html/')


# ************************************
#友情链接
@blue.route('/admin/ransflink/')
def rans_flink():
    
    return render_template('admin/flink.html/')

# 增加友情链接
@blue.route('/admin/addflink/')
def add_flink():
    
    return render_template('admin/add-flink.html/')


# 修改友情链接
@blue.route('/admin/updateflink/')
def update_flink():
    
    return render_template('admin/update-flink.html/')


#************************************
# 访问记录
@blue.route('/admin/ransloginlog/')
def rans_loginlog():
    
    return render_template('admin/loginlog.html/')

#删除访问记录


#**************************************
# 管理用户
@blue.route('/admin/manageuser/')
def manage_user():
    
    return render_template('admin/manage-user.html/')


# 常规设置
@blue.route('/admin/normalset/')
def normal_set():
    return render_template('admin/setting.html/')


# 用户设置
@blue.route('/admin/readset/')
def read_set():
    return render_template('admin/readset.html/')


#前台
#********************************************************
#网站首页
@blue.route('/')
def index():
    arts = ArtMoel.query.all()
    return render_template('home/index.html/',arts=arts)

#我的相册
@blue.route('/home/sharepic/')
def share_pic():
    
    return render_template('home/share.html')

#我的日记
@blue.route('/home/daylist/')
def day_list():
    #正向一查多,得到日记中所有文章
    arts = Category.query.get(3).arts
    return render_template('home/list.html',arts=arts)

#关于我
@blue.route('/home/abooutme/')
def about_me():
    
    return render_template('home/about.html')

#留言
@blue.route('/home/gbook/')
def g_book():
    
    return render_template('home/gbook.html')

#********************************
#查看内容页
@blue.route('/home/info/')
def in_fo():
    arts = ArtMoel.query.all()
    return render_template('home/info.html',arts=arts)

#查看日记
@blue.route('/home/geti/')
def get_i():
    arts = Category.query.get(3).arts
    return render_template('home/list.html',arts=arts)

#学无止境
@blue.route('/home/getn/')
def get_n():
    
    return render_template('home/info.html')

#慢生活
@blue.route('/home/getf/')
def get_f():
    return render_template('home/info.html')

#美文欣赏
@blue.route('/home/geto/')
def get_o():
    return render_template('home/info.html')

#图片详情
@blue.route('/home/infopic/')
def info_pic():
    return render_template('home/infopic.html')


