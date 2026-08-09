import re
import os

template = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - بوابة الطالب - MV TEACHES</title>
    <link rel="stylesheet" href="style.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
</head>
<body>
    <div class="portal-layout">
        <!-- Sidebar -->
        <aside class="sidebar">
            <div class="sidebar-header">
                <h2>MV <span>TEACHES</span></h2>
                <div class="student-badge">بوابة الطالب</div>
            </div>
            <nav class="sidebar-nav">
                <ul>
                    <li><a href="portal_dashboard.html" class="sidebar-link {a_dashboard}"><i class="fa-solid fa-border-all"></i> <span>الرئيسية (لوحة التحكم)</span></a></li>
                    <li><a href="portal_classes.html" class="sidebar-link {a_classes}"><i class="fa-solid fa-video"></i> <span>حصصي</span></a></li>
                    <li><a href="portal_attendance.html" class="sidebar-link {a_attendance}"><i class="fa-solid fa-calendar-check"></i> <span>سجل الحضور</span></a></li>
                    <li><a href="portal_apology.html" class="sidebar-link {a_apology}"><i class="fa-solid fa-envelope-open-text"></i> <span>طلب اعتذار عن حصة</span></a></li>
                    <li><a href="portal_finance.html" class="sidebar-link {a_finance}"><i class="fa-solid fa-file-invoice-dollar"></i> <span>حسابي المالي</span></a></li>
                    <li><a href="portal_test.html" class="sidebar-link {a_test}"><i class="fa-solid fa-file-signature"></i> <span>امتحان تحديد المستوى</span></a></li>
                    <li><a href="portal_progress.html" class="sidebar-link {a_progress}"><i class="fa-solid fa-award"></i> <span>تقدمي / الشهادات</span></a></li>
                    <li><a href="portal_profile.html" class="sidebar-link {a_profile}"><i class="fa-solid fa-user-gear"></i> <span>الملف الشخصي</span></a></li>
                </ul>
            </nav>
            <div class="sidebar-footer">
                <a href="index.html" class="btn btn-outline" style="width: 100%; border-color: rgba(255,255,255,0.3); color: white; display: block; text-align: center; text-decoration: none;">
                    <i class="fa-solid fa-arrow-right-from-bracket"></i> تسجيل الخروج
                </a>
            </div>
        </aside>

        <!-- Main Content -->
        <main class="portal-main">
            <header class="portal-header">
                <div class="header-search">
                    <h2 class="text-primary">مرحباً بك، أحمد 👋</h2>
                </div>
                <div class="user-profile-mini">
                    <div style="position: relative;">
                        <i class="fa-solid fa-bell" style="font-size: 1.2rem; color: var(--text-muted);"></i>
                        <span style="position: absolute; top: -5px; right: -5px; background: var(--danger); width: 8px; height: 8px; border-radius: 50%;"></span>
                    </div>
                    <div class="avatar" style="width: 40px; height: 40px; background: var(--secondary); color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold;">أ</div>
                </div>
            </header>
            <div class="portal-content fade-in">
                {content}
            </div>
        </main>
    </div>
</body>
</html>"""

pages = {
    'portal_dashboard.html': {
        'title': 'لوحة التحكم',
        'active_key': 'a_dashboard',
        'content': '''<!-- Overview Stats -->
                    <div class="dash-grid">
                        <div class="stat-card">
                            <div class="stat-icon"><i class="fa-solid fa-calendar-day"></i></div>
                            <div class="stat-info">
                                <h3>2</h3>
                                <p>حصص متبقية هذا الأسبوع</p>
                            </div>
                        </div>
                        <div class="stat-card" style="border-right-color: var(--success);">
                            <div class="stat-icon" style="color: var(--success);"><i class="fa-solid fa-circle-check"></i></div>
                            <div class="stat-info">
                                <h3>فعال</h3>
                                <p>حالة الاشتراك (ينتهي في 20/09)</p>
                            </div>
                        </div>
                        <div class="stat-card" style="border-right-color: var(--accent);">
                            <div class="stat-icon" style="color: var(--accent);"><i class="fa-solid fa-chart-line"></i></div>
                            <div class="stat-info">
                                <h3>B1</h3>
                                <p>المستوى الحالي</p>
                            </div>
                        </div>
                    </div>
    
                    <!-- Schedule Section (My Classes) -->
                    <div class="panel">
                        <div class="panel-header">
                            <div class="panel-title">حصصي القادمة (حسب توقيت الأردن)</div>
                            <a href="portal_classes.html" class="text-secondary font-weight-bold" style="text-decoration: none;">عرض الجدول الكامل</a>
                        </div>
                        
                        <div class="class-list">
                            <!-- Class 1: Active Zoom Link -->
                            <div class="class-item" style="border-right: 4px solid var(--success);">
                                <div class="class-info">
                                    <h4>محادثة متقدمة - Advanced Conversation</h4>
                                    <div class="class-meta">
                                        <span><i class="fa-regular fa-clock"></i> اليوم, 6:00 مساءً</span>
                                        <span><i class="fa-solid fa-chalkboard-user"></i> أ. سارة جونز (Sarah Jones)</span>
                                    </div>
                                </div>
                                <div class="class-action">
                                    <button class="btn btn-zoom">
                                        <span class="pulse-indicator"></span>
                                        انضمام (Zoom)
                                    </button>
                                </div>
                            </div>
                        </div>
                    </div>'''
    },
    'portal_classes.html': {
        'title': 'حصصي',
        'active_key': 'a_classes',
        'content': '''<h2 class="text-primary mb-4" style="margin-bottom: 20px;">جدول حصصي</h2>
                    <div class="panel">
                        <div class="class-list">
                            <div class="class-item" style="border-right: 4px solid var(--success);">
                                <div class="class-info">
                                    <h4>محادثة متقدمة - Advanced Conversation</h4>
                                    <div class="class-meta">
                                        <span><i class="fa-regular fa-clock"></i> اليوم, 6:00 مساءً</span>
                                        <span><i class="fa-solid fa-chalkboard-user"></i> أ. سارة جونز</span>
                                    </div>
                                </div>
                                <div class="class-action">
                                    <button class="btn btn-zoom"><span class="pulse-indicator"></span> انضمام (Zoom)</button>
                                </div>
                            </div>
                            <div class="class-item">
                                <div class="class-info">
                                    <h4>قواعد - Grammar B1</h4>
                                    <div class="class-meta">
                                        <span><i class="fa-regular fa-clock"></i> غداً, 4:30 مساءً</span>
                                        <span><i class="fa-solid fa-chalkboard-user"></i> أ. ديفيد سميث</span>
                                    </div>
                                </div>
                                <div class="class-action">
                                    <span class="text-muted" style="font-size: 0.9rem; opacity: 0.7;">يظهر الرابط قبل 15 دقيقة</span>
                                </div>
                            </div>
                        </div>
                    </div>'''
    },
    'portal_attendance.html': {
        'title': 'سجل الحضور',
        'active_key': 'a_attendance',
        'content': '''<h2 class="text-primary mb-4" style="margin-bottom: 20px;">سجل الحضور التاريخي</h2>
                    <div class="panel">
                        <table style="width: 100%; text-align: right; border-collapse: collapse;">
                            <thead>
                                <tr style="border-bottom: 2px solid #eee;">
                                    <th style="padding: 10px;">التاريخ</th>
                                    <th style="padding: 10px;">الحصة</th>
                                    <th style="padding: 10px;">المعلم</th>
                                    <th style="padding: 10px;">الحالة</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr style="border-bottom: 1px solid #eee;">
                                    <td style="padding: 15px 10px;">15/08/2026</td>
                                    <td>قواعد B1</td>
                                    <td>أ. ديفيد سميث</td>
                                    <td><span class="badge" style="background: var(--success); color: white;">حاضر</span></td>
                                </tr>
                                <tr style="border-bottom: 1px solid #eee;">
                                    <td style="padding: 15px 10px;">12/08/2026</td>
                                    <td>محادثة متقدمة</td>
                                    <td>أ. سارة جونز</td>
                                    <td><span class="badge" style="background: var(--warning); color: black;">مؤجلة (عذر)</span></td>
                                </tr>
                            </tbody>
                        </table>
                    </div>'''
    },
    'portal_apology.html': {
        'title': 'طلب اعتذار',
        'active_key': 'a_apology',
        'content': '''<h2 class="text-primary mb-4" style="margin-bottom: 20px;">طلب اعتذار عن غياب</h2>
                    <div class="panel" style="max-width: 600px;">
                        <p class="text-muted" style="margin-bottom: 20px;">سيتم قبول العذر تلقائياً إذا تم تقديمه قبل 12 ساعة من موعد الحصة.</p>
                        <form onsubmit="event.preventDefault(); alert('تم رفع العذر وسيتم مراجعته تلقائياً.'); window.location.href='portal_dashboard.html';">
                            <div class="form-group">
                                <label>اختر الحصة</label>
                                <select class="form-control">
                                    <option>قواعد - الغد 4:30 م</option>
                                    <option>استماع - الأربعاء 5:00 م</option>
                                </select>
                            </div>
                            <div class="form-group">
                                <label>سبب الاعتذار</label>
                                <textarea class="form-control" rows="4" placeholder="اكتب السبب هنا..." required></textarea>
                            </div>
                            <div class="form-group">
                                <label>إرفاق مستند (اختياري)</label>
                                <input type="file" class="form-control">
                            </div>
                            <button class="btn btn-secondary">إرسال العذر</button>
                        </form>
                    </div>'''
    },
    'portal_finance.html': {
        'title': 'حسابي المالي',
        'active_key': 'a_finance',
        'content': '''<h2 class="text-primary mb-4" style="margin-bottom: 20px;">حسابي المالي</h2>
                    <div class="panel" style="max-width: 600px;">
                        <div style="background: rgba(164, 16, 52, 0.05); padding: 20px; border-radius: 8px; border: 1px dashed var(--secondary);">
                            <h4 style="color: var(--primary); margin-bottom: 10px;">الباقة الفضية (الأردن)</h4>
                            <div style="display: flex; justify-content: space-between; margin-bottom: 15px;">
                                <span class="text-muted">المدفوعات السابقة</span>
                                <strong>120 JOD</strong>
                            </div>
                            <div style="display: flex; justify-content: space-between; margin-bottom: 20px;">
                                <span class="text-muted">تاريخ التجديد القادم</span>
                                <strong>20/09/2026</strong>
                            </div>
                            <button class="btn btn-primary" style="width: 100%; padding: 12px;" onclick="alert('توجيه إلى بوابة دفع الفرع...')">تجديد الاشتراك (بوابة الدفع)</button>
                        </div>
                    </div>'''
    },
    'portal_test.html': {
        'title': 'امتحان المستوى',
        'active_key': 'a_test',
        'content': '''<h2 class="text-primary mb-4" style="margin-bottom: 20px;">امتحان تحديد المستوى</h2>
                    <div class="panel text-center">
                        <i class="fa-solid fa-file-signature text-accent" style="font-size: 3rem; margin-bottom: 15px;"></i>
                        <h3>لقد أتممت امتحان تحديد المستوى</h3>
                        <p class="text-muted">مستواك الحالي هو: B1 Intermediate</p>
                    </div>'''
    },
    'portal_progress.html': {
        'title': 'التقدم والشهادات',
        'active_key': 'a_progress',
        'content': '''<h2 class="text-primary mb-4" style="margin-bottom: 20px;">تقدمي والشهادات</h2>
                    <div class="panel">
                        <h3>نسبة إنجاز المستوى B1</h3>
                        <div style="width: 100%; background: #eee; height: 10px; border-radius: 5px; margin: 15px 0;">
                            <div style="width: 75%; background: var(--success); height: 100%; border-radius: 5px;"></div>
                        </div>
                        <p class="text-muted" style="margin-bottom: 20px;">أنت على بعد خطوة من إتمام المستوى!</p>
                        
                        <h4>الشهادات السابقة</h4>
                        <div style="margin-top: 10px;">
                            <button class="btn btn-outline"><i class="fa-solid fa-download"></i> شهادة مستوى A2 (PDF)</button>
                        </div>
                    </div>'''
    },
    'portal_profile.html': {
        'title': 'الملف الشخصي',
        'active_key': 'a_profile',
        'content': '''<h2 class="text-primary mb-4" style="margin-bottom: 20px;">الملف الشخصي</h2>
                    <div class="panel" style="max-width: 600px;">
                        <form onsubmit="event.preventDefault(); alert('تم حفظ التعديلات');">
                            <div class="form-group"><label>الاسم</label><input type="text" class="form-control" value="أحمد"></div>
                            <div class="form-group"><label>البريد الإلكتروني</label><input type="email" class="form-control" value="ahmad@example.com"></div>
                            <div class="form-group"><label>تفضيلات التنبيهات</label>
                                <select class="form-control"><option>تنبيهات البريد والواتساب</option><option>واتساب فقط</option></select>
                            </div>
                            <button class="btn btn-secondary">حفظ التغييرات</button>
                        </form>
                    </div>'''
    }
}

for filename, data in pages.items():
    # Build dictionary with default empty strings for active classes
    format_dict = {
        'title': data['title'],
        'content': data['content'],
        'a_dashboard': '',
        'a_classes': '',
        'a_attendance': '',
        'a_apology': '',
        'a_finance': '',
        'a_test': '',
        'a_progress': '',
        'a_profile': ''
    }
    # Set the active class
    format_dict[data['active_key']] = 'active'
    
    html_output = template.format(**format_dict)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html_output)

print("Created all pages.")
