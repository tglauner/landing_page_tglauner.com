Note that the directory structure in production is as follows:

Path is: /var/www/html

find . \
  -type d \( -name .git -o -name node_modules -o -name sessions \) -prune -o \
  -maxdepth 3 -mindepth 1 -exec ls -ld {} +

root: html# find . \
  -type d \( -name .git -o -name node_modules -o -name sessions \) -prune -o \
  -maxdepth 3 -mindepth 1 -exec ls -ld {} +
find: warning: you have specified the global option -maxdepth after the argument -type, but global options are not positional, i.e., -maxdepth affects tests specified before it as well as those specified after it.  Please specify global options before other arguments.
find: warning: you have specified the global option -mindepth after the argument -type, but global options are not positional, i.e., -mindepth affects tests specified before it as well as those specified after it.  Please specify global options before other arguments.
-rw-r--r--  1 root     root          378 Jul 29 21:42  ./.gitignore
-rw-r--r--  1 root     root           25 Jul 29 21:53  ./.htaccess
-rw-r--r--  1 root     root           27 Jul 29 21:42  ./README.md
drwxr-xr-x 10 root     root         4096 Sep 20 23:42  ./ai_value_advisor
-rw-r--r--  1 root     root           62 Sep  6 16:15  ./ai_value_advisor/.env
-rw-r--r--  1 root     root          584 Sep  6 16:14  ./ai_value_advisor/.env.bak
-rw-r--r--  1 root     root           62 Sep  6 19:39  ./ai_value_advisor/.env.pre-patch
-rw-r--r--  1 root     root         4752 Aug 29 21:40  ./ai_value_advisor/.gitignore
drwxr-xr-x  5 root     root         4096 Aug 25 22:30  ./ai_value_advisor/.venv
drwxr-xr-x  2 root     root         4096 Sep 10 12:24  ./ai_value_advisor/.venv/bin
drwxr-xr-x  4 root     root         4096 Aug 25 22:31  ./ai_value_advisor/.venv/include
drwxr-xr-x  3 root     root         4096 Aug 25 22:30  ./ai_value_advisor/.venv/lib
lrwxrwxrwx  1 root     root            3 Aug 25 22:30  ./ai_value_advisor/.venv/lib64 -> lib
-rw-r--r--  1 root     root          175 Aug 25 22:30  ./ai_value_advisor/.venv/pyvenv.cfg
-rw-r--r--  1 root     root         1656 Sep 10 12:22  ./ai_value_advisor/AGENTS.md
-rw-r--r--  1 root     root         4654 Sep 20 23:42  ./ai_value_advisor/README.md
drwxr-xr-x  3 root     root         4096 Sep 10 12:34  ./ai_value_advisor/backend
-rw-r--r--  1 root     root          780 Sep 10 12:34  ./ai_value_advisor/backend/.env
-rw-r--r--  1 root     root          645 Sep 10 12:22  ./ai_value_advisor/backend/.env.example
-rw-r--r--  1 root     root          585 Sep  6 19:39  ./ai_value_advisor/backend/.env.pre-patch
drwxr-xr-x  2 root     root         4096 Aug 29 23:08  ./ai_value_advisor/backend/__pycache__
-rw-r--r--  1 root     root         1438 Sep  7 14:08  ./ai_value_advisor/backend/auth.py
-rw-r--r--  1 root     root          829 Sep 10 12:22  ./ai_value_advisor/backend/config.py
-rw-r--r--  1 root     root          649 Aug 25 12:33  ./ai_value_advisor/backend/database.py
-rw-r--r--  1 root     root         3305 Sep 10 12:22  ./ai_value_advisor/backend/main.py
-rw-r--r--  1 root     root          440 Aug 25 12:33  ./ai_value_advisor/backend/models.py
-rw-r--r--  1 root     root          967 Sep 10 12:22  ./ai_value_advisor/backend/openai_client.py
-rw-r--r--  1 root     root          393 Sep 10 12:22  ./ai_value_advisor/backend/schemas.py
drwxrwx---  2 www-data www-data     4096 Aug 30 16:14  ./ai_value_advisor/data
-rw-r--r--  1 www-data www-data    32768 Aug 30 16:14  ./ai_value_advisor/data/app.db
-rwxr-xr-x  1 root     root           67 Sep 10 12:22  ./ai_value_advisor/debug_print_setup.sh
drwxr-xr-x  2 root     root         4096 Sep 10 12:22  ./ai_value_advisor/deploy
-rw-r--r--  1 root     root          370 Sep 10 12:22  ./ai_value_advisor/deploy/ai-value-advisor.service
-rw-r--r--  1 root     root          703 Aug 29 22:22  ./ai_value_advisor/deploy/apache.conf
drwxr-xr-x  6 root     root         4096 Sep 20 23:43  ./ai_value_advisor/frontend
-rw-r--r--  1 root     root          103 Sep  6 19:42  ./ai_value_advisor/frontend/.env
-rw-r--r--  1 root     root          260 Sep 10 12:22  ./ai_value_advisor/frontend/.env.example
-rw-r--r--  1 root     root         5953 Aug 26 00:47  ./ai_value_advisor/frontend/app.js
drwxr-xr-x  3 root     root         4096 Sep 20 23:43  ./ai_value_advisor/frontend/dist
-rw-r--r--  1 root     root         9985 Sep 20 23:42  ./ai_value_advisor/frontend/index.html
-rw-r--r--  1 root     root        52965 Sep 20 23:43  ./ai_value_advisor/frontend/package-lock.json
-rw-r--r--  1 root     root          341 Aug 29 20:53  ./ai_value_advisor/frontend/package.json
drwxr-xr-x  2 root     root         4096 Sep 10 12:22  ./ai_value_advisor/frontend/public
drwxr-xr-x  2 root     root         4096 Sep 10 12:22  ./ai_value_advisor/frontend/src
-rw-r--r--  1 root     root          677 Sep  6 20:15  ./ai_value_advisor/frontend/vite.config.js
-rw-r--r--  1 root     root        36740 Aug 26 00:41  ./ai_value_advisor/package-lock.json
-rw-r--r--  1 root     root          127 Aug 26 00:41  ./ai_value_advisor/package.json
-rw-r--r--  1 root     root           97 Sep 10 12:22  ./ai_value_advisor/requirements.txt
drwxr-xr-x  2 root     root         4096 Sep  7 14:08  ./ai_value_advisor/tests
-rw-r--r--  1 root     root         1963 Sep  7 14:08  ./ai_value_advisor/tests/test_auth.py
drwxr-xr-x  2 root     root         4096 Jul 29 21:42  ./assets
-rw-r--r--  1 root     root       135398 Jul 29 21:42  ./assets/derivatives-course.jpg
-rw-r--r--  1 root     root      1031986 Jul 29 21:42  ./assets/favicon.png
-rw-r--r--  1 root     root       147611 Jul 29 21:42  ./assets/frtb-course.jpg
-rw-r--r--  1 root     root       118842 Jul 29 21:42  ./assets/hero-bg.jpg
-rw-r--r--  1 root     root       175157 Jul 29 21:42  ./assets/mbs-course.jpg
-rw-r--r--  1 root     root         4126 Jul 29 21:42  ./assets/react.svg
drwxr-xr-x  8 root     root         4096 Sep 21 12:08  ./course_xva_essentials
-rw-r--r--  1 root     root          163 Sep 16 04:07  ./course_xva_essentials/.gitignore
drwxr-xr-x  5 root     root         4096 Sep  2 14:44  ./course_xva_essentials/.venv
drwxr-xr-x  2 root     root         4096 Sep  2 14:44  ./course_xva_essentials/.venv/bin
drwxr-xr-x  3 root     root         4096 Sep  2 14:44  ./course_xva_essentials/.venv/include
drwxr-xr-x  3 root     root         4096 Sep  2 14:44  ./course_xva_essentials/.venv/lib
lrwxrwxrwx  1 root     root            3 Sep  2 14:44  ./course_xva_essentials/.venv/lib64 -> lib
-rw-r--r--  1 root     root          180 Sep  2 14:44  ./course_xva_essentials/.venv/pyvenv.cfg
-rw-r--r--  1 root     root         4076 Sep 21 12:08  ./course_xva_essentials/README.md
drwxr-xr-x  2 root     root         4096 Sep 16 04:07  ./course_xva_essentials/backend
-rw-r--r--  1 root     root          673 Sep 16 04:07  ./course_xva_essentials/backend/main.py
-rw-r--r--  1 root     root           16 Sep 16 04:07  ./course_xva_essentials/backend/requirements.txt
-rw-r--r--  1 root     root         6214 Sep 16 16:22  ./course_xva_essentials/course_delivery_summary.md
-rw-r--r--  1 root     root        58114 Sep 16 04:07  ./course_xva_essentials/course_materials.md
-rw-r--r--  1 root     root         5224 Sep  2 10:58  ./course_xva_essentials/course_outline.md
-rw-r--r--  1 root     root         1216 Sep  2 10:58  ./course_xva_essentials/debug_findings.md
drwxr-xr-x  2 root     root         4096 Sep 21 12:08  ./course_xva_essentials/deploy
-rw-r--r--  1 root     root          722 Sep 21 12:08  ./course_xva_essentials/deploy/apache.conf
-rw-r--r--  1 root     root          208 Sep 21 12:08  ./course_xva_essentials/deploy/course-xva-essentials-redirect.conf
-rw-r--r--  1 root     root          540 Sep 21 12:08  ./course_xva_essentials/deploy/course-xva-essentials.conf
-rw-r--r--  1 root     root         9589 Sep 16 16:22  ./course_xva_essentials/enhanced_course_delivery_summary.md
drwxr-xr-x  5 www-data www-data     4096 Sep 21 12:30  ./course_xva_essentials/frontend
-rwxr-xr-x  1 www-data www-data       91 Sep 16 16:25  ./course_xva_essentials/frontend/.env
-rwxr-xr-x  1 www-data www-data       54 Sep 16 04:07  ./course_xva_essentials/frontend/.env.example
-rwxr-xr-x  1 www-data www-data      424 Sep  2 20:00  ./course_xva_essentials/frontend/components.json
drwxr-xr-x  3 www-data www-data     4096 Sep 22 12:13  ./course_xva_essentials/frontend/dist
-rwxr-xr-x  1 www-data www-data      441 Sep 21 12:08  ./course_xva_essentials/frontend/index.html
-rwxr-xr-x  1 www-data www-data     2682 Sep 16 16:32  ./course_xva_essentials/frontend/package.json
-rwxr-xr-x  1 www-data www-data      114 Sep 16 16:41  ./course_xva_essentials/frontend/pnpm-lock.yaml
drwxr-xr-x  2 www-data www-data     4096 Sep  2 20:00  ./course_xva_essentials/frontend/public
drwxr-xr-x  6 www-data www-data     4096 Sep 20 12:17  ./course_xva_essentials/frontend/src
-rwxr-xr-x  1 www-data www-data      413 Sep 16 16:22  ./course_xva_essentials/frontend/vite.config.js
-rwxr-xr-x  1 www-data www-data      522 Sep 16 04:06  ./course_xva_essentials/frontend/vite.config.js.bak
drwxr-xr-x  2 root     root         4096 Sep 16 04:07  ./course_xva_essentials/latex_material
-rw-r--r--  1 root     root        41532 Sep 16 04:07  ./course_xva_essentials/latex_material/xva_course.tex
-rw-r--r--  1 root     root         8108 Sep 16 16:22  ./course_xva_essentials/paywall_implementation_summary.md
drwxr-xr-x  3 root     www-data     4096 Aug 22 05:04  ./dashboard
drwxr-xr-x  3 root     root         4096 Aug 22 15:55  ./dashboard/dist
drwxr-xr-x  2 root     root         4096 Aug 22 20:43  ./dashboard/dist/assets
-rw-r--r--  1 root     root        15406 Aug 22 20:43  ./dashboard/dist/favicon.ico
-rw-r--r--  1 root     root      1005554 Aug 22 20:43  ./dashboard/dist/favicon.png
-rw-r--r--  1 root     root          523 Aug 22 20:43  ./dashboard/dist/index.html
drwxr-xr-x  2 www-data www-data     4096 Nov 29 17:36  ./data
-rw-r--r--  1 www-data www-data    28672 Nov 29 17:36  ./data/app.db
-rw-r--r--  1 root     root        15406 Jul 29 21:42  ./favicon.ico
drwxr-xr-x  5 root     root         4096 Jan 13 13:35  ./frtb_fundamentals
-rw-r--r--  1 root     root            9 Jul 11  2025  ./frtb_fundamentals/.gitignore
-rw-r--r--  1 root     root     10328147 Jul 10  2025  ./frtb_fundamentals/Archive.zip
-rw-r--r--  1 root     root       164855 Jul 10  2025 './frtb_fundamentals/File-Based Analytics Tracking Documentation.pdf'
-rw-r--r--  1 root     root          112 Jul 10  2025  ./frtb_fundamentals/README.md
-rw-r--r--  1 root     root        12535 Jul 10  2025  ./frtb_fundamentals/analytics.js
-rw-r--r--  1 root     root         6079 Jul 10  2025  ./frtb_fundamentals/analytics_data.json
-rw-r--r--  1 root     root         3550 Dec 11 10:34  ./frtb_fundamentals/calc_frtb_sa_charge_for_1_swap.py
-rw-r--r--  1 root     root         3504 Jan 13 13:35  ./frtb_fundamentals/content_outline.md
-rw-r--r--  1 root     root        10134 Jul 10  2025  ./frtb_fundamentals/cookie-consent.js
-rw-r--r--  1 root     root        12182 Jul 27 00:41  ./frtb_fundamentals/cookie-policy.html
-rw-r--r--  1 root     root         5118 Jul 10  2025  ./frtb_fundamentals/cookie-styles.css
-rw-r--r--  1 root     root         3440 Jan 13 13:35  ./frtb_fundamentals/documentation.md
-rw-r--r--  1 root     root         5211 Jul 10  2025  ./frtb_fundamentals/file_based_analytics_documentation.md
-rw-r--r--  1 root     root         2179 Jul 10  2025  ./frtb_fundamentals/footer.html
-rw-r--r--  1 root     root          376 Jul 10  2025  ./frtb_fundamentals/footer.js
-rw-r--r--  1 root     root         4458 Jan 13 13:35  ./frtb_fundamentals/geo-redirect.js
drwxr-xr-x  2 root     root         4096 Jul 27 00:41  ./frtb_fundamentals/images
-rw-r--r--  1 root     root       405960 Jul 27 00:41 './frtb_fundamentals/images/319 slides 2.1-14 2 tests looks great 2.1.jpg'
-rw-r--r--  1 root     root      1024092 Jul 27 00:41  ./frtb_fundamentals/images/FRTB_favicon.png
-rw-r--r--  1 root     root      1038086 Jul 10  2025  ./frtb_fundamentals/images/IRD_favicon.png
-rw-r--r--  1 root     root       597811 Jul 10  2025  ./frtb_fundamentals/images/TGIR_simple_chatbot_only_logo.png
-rwxr-xr-x  1 root     root       514529 Jul 10  2025  ./frtb_fundamentals/images/ficc_trading_floor.png
-rw-r--r--  1 root     root      7444313 Jul 10  2025  ./frtb_fundamentals/images/frtb_skyline.jpg
-rw-r--r--  1 root     root       310913 Jul 10  2025  ./frtb_fundamentals/images/instructor.jpg
-rw-r--r--  1 root     root       329610 Jul 10  2025  ./frtb_fundamentals/images/preview_lesson.jpg
-rw-r--r--  1 root     root        31216 Jan 13 13:35  ./frtb_fundamentals/index.html
-rw-r--r--  1 root     root        52191 Dec 11 10:34  ./frtb_fundamentals/one_USD_SOFR_swap_reconciliation.xlsx
-rw-r--r--  1 root     root        11413 Jan 13 13:35  ./frtb_fundamentals/pre-checkout.html
-rw-r--r--  1 root     root        12831 Jul 27 00:41  ./frtb_fundamentals/privacy-policy.html
-rw-r--r--  1 root     root         4702 Jan 13 13:35  ./frtb_fundamentals/research_findings.md
-rw-r--r--  1 root     root         4898 Jul 10  2025  ./frtb_fundamentals/script.js
-rw-r--r--  1 root     root        16666 Jul 10  2025  ./frtb_fundamentals/styles.css
-rw-r--r--  1 root     root        13845 Jul 10  2025  ./frtb_fundamentals/terms-of-service.html
-rw-r--r--  1 root     root         1174 Jul 10  2025  ./frtb_fundamentals/todo.md
-rw-r--r--  1 root     root         6039 Jul 10  2025  ./frtb_fundamentals/track.php
-rw-r--r--  1 root     root        29734 Jan 13 13:34  ./golden_selling.html
-rw-r--r--  1 root     root        49552 Jan 13 23:41  ./index.html
drwxrwxr-x  5 root     www-data     4096 Jan 13 13:35  ./mastering_interest_rate_derivatives
-rw-r--r--  1 root     root           58 Jul 25 01:57  ./mastering_interest_rate_derivatives/.gitignore
-rw-rw-r--  1 root     www-data   164855 Jul 25 01:57 './mastering_interest_rate_derivatives/File-Based Analytics Tracking Documentation.pdf'
-rw-rw-r--  1 root     www-data      112 Jul 25 01:57  ./mastering_interest_rate_derivatives/README.md
-rw-r--r--  1 root     root        12535 Jul 25 01:57  ./mastering_interest_rate_derivatives/analytics.js
-rw-r--r--  1 www-data www-data    81107 Jan 13 23:33  ./mastering_interest_rate_derivatives/analytics_data.json
-rw-r--r--  1 root     root         3504 Jan 13 13:35  ./mastering_interest_rate_derivatives/content_outline.md
-rw-rw-r--  1 root     www-data    11265 Jul 25 01:57  ./mastering_interest_rate_derivatives/cookie-consent.js
-rw-r--r--  1 root     root        12432 Jul 25 01:57  ./mastering_interest_rate_derivatives/cookie-policy.html
-rw-rw-r--  1 root     www-data     5427 Jul 25 01:57  ./mastering_interest_rate_derivatives/cookie-styles.css
-rw-r--r--  1 root     root         3440 Jan 13 13:35  ./mastering_interest_rate_derivatives/documentation.md
-rw-r--r--  1 root     root         5211 Jul 25 01:57  ./mastering_interest_rate_derivatives/file_based_analytics_documentation.md
-rw-r--r--  1 root     root         2174 Jul 25 01:57  ./mastering_interest_rate_derivatives/footer.html
-rw-r--r--  1 root     root          378 Jul 25 01:57  ./mastering_interest_rate_derivatives/footer.js
-rw-r--r--  1 root     root         4459 Jan 13 13:35  ./mastering_interest_rate_derivatives/geo-redirect.js
drwxrwxr-x  2 root     www-data     4096 Jul 25 01:59  ./mastering_interest_rate_derivatives/images
-rw-r--r--  1 root     root      1038086 Jul 25 01:57  ./mastering_interest_rate_derivatives/images/IRD_favicon.png
-rw-rw-r--  1 root     www-data   597811 Jul 25 01:57  ./mastering_interest_rate_derivatives/images/TGIR_simple_chatbot_only_logo.png
-rw-r--r--  1 root     root       514529 Jul 25 01:59  ./mastering_interest_rate_derivatives/images/ficc_trading_floor.png
-rw-rw-r--  1 root     www-data   310913 Jul 25 01:57  ./mastering_interest_rate_derivatives/images/instructor.jpg
-rw-rw-r--  1 root     www-data   329610 Jul 25 01:57  ./mastering_interest_rate_derivatives/images/preview_lesson.jpg
-rw-r--r--  1 root     root        29617 Jan 13 13:35  ./mastering_interest_rate_derivatives/index.html
-rw-r--r--  1 root     root        11413 Jan 13 13:35  ./mastering_interest_rate_derivatives/pre-checkout.html
-rw-r--r--  1 root     root        12930 Jul 25 01:57  ./mastering_interest_rate_derivatives/privacy-policy.html
-rw-r--r--  1 root     root         4702 Jan 13 13:35  ./mastering_interest_rate_derivatives/research_findings.md
-rw-rw-r--  1 root     www-data     5339 Jul 25 01:57  ./mastering_interest_rate_derivatives/script.js
-rw-r--r--  1 root     root        16473 Jul 25 01:57  ./mastering_interest_rate_derivatives/styles.css
-rw-r--r--  1 root     root        13845 Jul 25 01:57  ./mastering_interest_rate_derivatives/terms-of-service.html
-rw-rw-r--  1 root     www-data     1174 Jul 25 01:57  ./mastering_interest_rate_derivatives/todo.md
-rw-r--r--  1 root     root         6039 Jul 25 01:57  ./mastering_interest_rate_derivatives/track.php
drwxrwxr-x  4 root     www-data     4096 Jan 13 13:36  ./mastering_mbs_and_abs
-rw-rw-r--  1 root     www-data       39 Jun 10  2025  ./mastering_mbs_and_abs/.gitignore
-rw-rw-r--  1 root     www-data    10189 Jun  8  2025  ./mastering_mbs_and_abs/analytics.js
-rwxrwxrwx  1 root     root       221845 Jan 16 17:18  ./mastering_mbs_and_abs/analytics_data.json
-rw-r--r--  1 www-data www-data       46 Oct 10 20:10  ./mastering_mbs_and_abs/analytics_errors.log
-rw-rw-r--  1 root     www-data    11189 Jun  8  2025  ./mastering_mbs_and_abs/cookie-consent.js
-rw-r--r--  1 root     root        12163 Jun 15  2025  ./mastering_mbs_and_abs/cookie-policy.html
-rw-rw-r--  1 root     www-data     4806 Jun  8  2025  ./mastering_mbs_and_abs/cookie-styles.css
-rw-r--r--  1 root     root         2155 Jun 15  2025  ./mastering_mbs_and_abs/footer.html
-rw-r--r--  1 root     root          377 Jun 15  2025  ./mastering_mbs_and_abs/footer.js
-rw-r--r--  1 root     root         6754 Jan 13 13:36  ./mastering_mbs_and_abs/geo-redirect.js
drwxrwxr-x  2 root     www-data     4096 Jun 15  2025  ./mastering_mbs_and_abs/images
-rw-r--r--  1 root     root      1067290 Jun 15  2025  ./mastering_mbs_and_abs/images/MBS_favicon.png
-rw-rw-r--  1 root     www-data   597811 Jun 10  2025  ./mastering_mbs_and_abs/images/TGIR_simple_chatbot_only_logo.png
-rw-rw-r--  1 root     www-data   250726 Jun 10  2025  ./mastering_mbs_and_abs/images/mbs_course_logo.jpg
-rw-rw-r--  1 root     www-data   290890 Jun 10  2025  ./mastering_mbs_and_abs/images/multi-screens.png
-rw-rw-r--  1 root     www-data   609570 Jun 10  2025  ./mastering_mbs_and_abs/images/my_head.jpeg
-rw-rw-r--  1 root     www-data   195346 Jun  8  2025  ./mastering_mbs_and_abs/images/video-preview.jpg
-rw-r--r--  1 root     root        30705 Jan 13 13:36  ./mastering_mbs_and_abs/index.html
-rw-r--r--  1 root     root         8317 Jun 15  2025  ./mastering_mbs_and_abs/pre-checkout.html
-rw-r--r--  1 root     root        12403 Jun 15  2025  ./mastering_mbs_and_abs/privacy-policy.html
-rw-rw-r--  1 root     www-data     3740 Jun  8  2025  ./mastering_mbs_and_abs/script.js
-rw-r--r--  1 root     root        13966 Jun 15  2025  ./mastering_mbs_and_abs/styles.css
-rw-r--r--  1 root     root        14000 Jun 17  2025  ./mastering_mbs_and_abs/terms-of-service.html
-rw-rw-r--  1 root     www-data     4359 Jun  8  2025  ./mastering_mbs_and_abs/track.php
drwxr-xr-x  6 root     root         4096 Jan 12 01:56  ./mcp.tglauner.com
-rw-r--r--  1 root     root         4771 Jan 12 01:37  ./mcp.tglauner.com/.gitignore
drwxr-xr-x  2 root     root         4096 Jan 12 01:37  ./mcp.tglauner.com/.vscode
-rw-r--r--  1 root     root           37 Jan 12 01:37  ./mcp.tglauner.com/.vscode/settings.json
-rw-r--r--  1 root     root         2293 Jan 12 01:56  ./mcp.tglauner.com/README.md
-rw-r--r--  1 root     root        54095 Jan 12 01:37  ./mcp.tglauner.com/package-lock.json
-rw-r--r--  1 root     root          398 Jan 12 01:37  ./mcp.tglauner.com/package.json
-rw-r--r--  1 root     root         1981 Jan 12 01:37  ./mcp.tglauner.com/specs.json
drwxr-xr-x  2 root     root         4096 Jan 12 01:37  ./mcp.tglauner.com/src
-rw-r--r--  1 root     root         3328 Jan 12 01:37  ./mcp.tglauner.com/src/server.js
drwxr-xr-x  8 root     root         4096 Sep 13 12:58  ./multi_model_talkshow
-rw-------  1 www-data www-data      735 Sep  1 18:46  ./multi_model_talkshow/.env
-rw-r--r--  1 root     root          612 Sep  1 18:45  ./multi_model_talkshow/.env.example
-rw-r--r--  1 root     root          357 Aug 30 19:42  ./multi_model_talkshow/.gitignore
drwxr-xr-x  5 root     root         4096 Sep 13 10:31  ./multi_model_talkshow/.venv
drwxr-xr-x  2 root     root         4096 Sep 13 10:31  ./multi_model_talkshow/.venv/bin
drwxr-xr-x  4 root     root         4096 Sep 13 10:31  ./multi_model_talkshow/.venv/include
drwxr-xr-x  3 root     root         4096 Sep 13 10:31  ./multi_model_talkshow/.venv/lib
lrwxrwxrwx  1 root     root            3 Sep 13 10:31  ./multi_model_talkshow/.venv/lib64 -> lib
-rw-r--r--  1 root     root          179 Sep 13 10:31  ./multi_model_talkshow/.venv/pyvenv.cfg
-rw-r--r--  1 root     root         1600 Aug 30 19:42  ./multi_model_talkshow/AGENT.md
-rw-r--r--  1 root     root         4077 Sep 13 10:29  ./multi_model_talkshow/README.md
drwxr-xr-x  9 root     root         4096 Sep  1 18:45  ./multi_model_talkshow/backend
-rw-r--r--  1 root     root            0 Aug 30 19:42  ./multi_model_talkshow/backend/__init__.py
drwxr-xr-x  2 root     root         4096 Aug 30 21:04  ./multi_model_talkshow/backend/__pycache__
drwxr-xr-x  2 root     root         4096 Sep  1 22:36  ./multi_model_talkshow/backend/adapters
drwxr-xr-x  2 root     root         4096 Sep  1 00:24  ./multi_model_talkshow/backend/config
drwxr-xr-x  3 root     root         4096 Sep  1 12:59  ./multi_model_talkshow/backend/core
-rw-r--r--  1 root     root         1979 Sep  1 18:45  ./multi_model_talkshow/backend/main.py
drwxr-xr-x  3 root     root         4096 Aug 30 20:42  ./multi_model_talkshow/backend/models
drwxr-xr-x  3 root     root         4096 Sep  1 14:26  ./multi_model_talkshow/backend/routes
drwxr-xr-x  3 root     root         4096 Aug 30 19:42  ./multi_model_talkshow/backend/static
drwxr-xr-x  2 www-data www-data     4096 Aug 30 20:50  ./multi_model_talkshow/data
-rw-r--r--  1 www-data www-data    16384 Jan 13 13:34  ./multi_model_talkshow/data/app.db
drwxr-xr-x  2 root     root         4096 Sep  1 00:24  ./multi_model_talkshow/deploy
-rw-r--r--  1 root     root          771 Aug 30 20:41  ./multi_model_talkshow/deploy/apache.conf
-rw-r--r--  1 root     root          413 Sep  1 00:24  ./multi_model_talkshow/deploy/multi_model_talkshow.service
drwxr-xr-x  6 root     root         4096 Sep 25 12:47  ./multi_model_talkshow/frontend
-rw-r--r--  1 root     root          212 Aug 30 22:17  ./multi_model_talkshow/frontend/.env
-rw-r--r--  1 root     root          253 Sep  1 00:24  ./multi_model_talkshow/frontend/.env.example
-rw-r--r--  1 root     root          424 Aug 30 19:42  ./multi_model_talkshow/frontend/components.json
drwxr-xr-x  3 root     root         4096 Sep 25 12:47  ./multi_model_talkshow/frontend/dist
-rw-r--r--  1 root     root          844 Aug 30 19:42  ./multi_model_talkshow/frontend/eslint.config.js
-rw-r--r--  1 root     root          377 Aug 30 19:42  ./multi_model_talkshow/frontend/index.html
-rw-r--r--  1 root     root           95 Aug 30 19:42  ./multi_model_talkshow/frontend/jsconfig.json
-rw-r--r--  1 root     root      2132404 Aug 30 19:42  ./multi_model_talkshow/frontend/npm-debug.log
-rw-r--r--  1 root     root       202306 Sep 20 23:44  ./multi_model_talkshow/frontend/package-lock.json
-rw-r--r--  1 root     root         2571 Aug 30 19:42  ./multi_model_talkshow/frontend/package.json
-rw-r--r--  1 root     root       182534 Aug 30 19:42  ./multi_model_talkshow/frontend/pnpm-lock.yaml
drwxr-xr-x  2 root     root         4096 Aug 30 19:42  ./multi_model_talkshow/frontend/public
drwxr-xr-x  6 root     root         4096 Sep 13 10:29  ./multi_model_talkshow/frontend/src
-rw-r--r--  1 root     root          414 Aug 30 19:42  ./multi_model_talkshow/frontend/vite.config.js
-rw-r--r--  1 root     root          187 Sep 13 10:29  ./multi_model_talkshow/requirements.txt
-rw-r--r--  1 root     root           42 Aug  2 11:49  ./robots.txt
-rwxr-xr-x  1 root     root         3752 Jun 30  2025  ./send_daily_analytics.sh
-rw-r--r--  1 root     root          782 Aug 30 23:02  ./sitemap.xml
-rw-r--r--  1 root     root        17540 Jan 13 23:41  ./styles.css
drwxrwxr-x  2 root     www-data     4096 May 29  2025  ./tracking
-rw-rw-r--  1 root     www-data     2188 May 29  2025  ./tracking/classify_opens.py
-rw-rw-r--  1 root     www-data      323 May 23  2025  ./tracking/log.php
-rw-rw-r--  1 root     www-data    60214 Jun 11  2025  ./tracking/opens.csv
-rw-rw-r--  1 root     www-data      106 May 22  2025  ./tracking/pixel_1x1.png
drwxr-xr-x 11 root     root         4096 Sep 24 05:14  ./visitor_analytics
-rw-r--r--  1 root     root          445 Aug 17 08:16  ./visitor_analytics/.gitignore
drwxr-xr-x  5 root     root         4096 Sep 21 23:07  ./visitor_analytics/.venv
drwxr-xr-x  2 root     root         4096 Sep 21 23:08  ./visitor_analytics/.venv/bin
drwxr-xr-x  3 root     root         4096 Sep 21 23:07  ./visitor_analytics/.venv/include
drwxr-xr-x  3 root     root         4096 Sep 21 23:07  ./visitor_analytics/.venv/lib
lrwxrwxrwx  1 root     root            3 Sep 21 23:07  ./visitor_analytics/.venv/lib64 -> lib
-rw-r--r--  1 root     root          176 Sep 21 23:07  ./visitor_analytics/.venv/pyvenv.cfg
-rw-r--r--  1 root     root           74 Aug 17 08:16  ./visitor_analytics/DOCS.md
-rw-r--r--  1 root     root         2610 Aug 17 08:16  ./visitor_analytics/MAINTENANCE.md
-rw-r--r--  1 root     root          288 Aug 17 08:16  ./visitor_analytics/Makefile
-rw-r--r--  1 root     root         8628 Sep 24 05:14  ./visitor_analytics/README.md
drwxr-xr-x  5 root     root         4096 Sep 24 05:55  ./visitor_analytics/collector
-rw-r--r--  1 root     root          193 Aug 17 08:28  ./visitor_analytics/collector/.env
-rw-r--r--  1 root     root          162 Aug 17 08:16  ./visitor_analytics/collector/.env.example
-rw-r--r--  1 root     root            0 Sep 24 05:53  ./visitor_analytics/collector/__init__.py
-rw-r--r--  1 root     root        32768 Aug 17 08:16  ./visitor_analytics/collector/analytics.sqlite3-shm
-rw-r--r--  1 root     root       296672 Aug 17 08:16  ./visitor_analytics/collector/analytics.sqlite3-wal
-rw-r--r--  1 root     root        17180 Sep 24 05:53  ./visitor_analytics/collector/app.py
drwxr-xr-x  2 root     root         4096 Sep 25 02:24  ./visitor_analytics/collector/config
drwxr-xr-x  2 root     root         4096 Aug 17 08:16  ./visitor_analytics/collector/importer
drwxr-xr-x  2 root     root         4096 Aug 24 05:42  ./visitor_analytics/collector/migrations
-rw-r--r--  1 root     root         3938 Sep 24 05:14  ./visitor_analytics/collector/reporting_filters.py
-rw-r--r--  1 root     root          137 Aug 17 08:16  ./visitor_analytics/collector/requirements.txt
drwxrwxr-x  2 www-data www-data     4096 Sep 23 00:11  ./visitor_analytics/data
-rwxrwxrwx  1 www-data www-data  1679360 Jan 15 16:50  ./visitor_analytics/data/analytics.sqlite3
-rw-r--r--  1 www-data www-data    32768 Jan 19 00:59  ./visitor_analytics/data/analytics.sqlite3-shm
-rw-r--r--  1 www-data www-data  4223032 Jan 18 23:46  ./visitor_analytics/data/analytics.sqlite3-wal
drwxr-xr-x  2 root     root         4096 Nov 27 14:11  ./visitor_analytics/deploy
-rw-r--r--  1 root     root          869 Aug 24 05:42  ./visitor_analytics/deploy/README.md
-rw-r--r--  1 root     root          786 Sep 21 22:49  ./visitor_analytics/deploy/apache_snippet.conf
-rw-r--r--  1 root     root          603 Nov 27 14:11  ./visitor_analytics/deploy/collector.service
-rw-r--r--  1 root     root          162 Aug 17 08:16  ./visitor_analytics/deploy/env.example
drwxr-xr-x  2 root     root         4096 Aug 17 08:18  ./visitor_analytics/geo
-rw-r--r--  1 root     root         3199 Aug 17 08:16  ./visitor_analytics/initial_prompt.txt
drwxr-xr-x  2 root     root         4096 Aug 17 08:16  ./visitor_analytics/scripts
-rw-r--r--  1 root     root          206 Aug 17 08:16  ./visitor_analytics/scripts/dev.sh
-rw-r--r--  1 root     root           27 Aug 17 08:16  ./visitor_analytics/scripts/refresh_rollups.sh
drwxr-xr-x  3 root     root         4096 Sep 22 22:57  ./visitor_analytics/tracking
drwxr-xr-x  2 root     root         4096 Sep 21 22:49  ./visitor_analytics/tracking/apps
-rw-r--r--  1 root     root         6962 Sep 22 22:57  ./visitor_analytics/tracking/tracking.js
drwxr-xr-x  2 root     root         4096 Nov 27 14:11  ./visitor_analytics/visitor_log
-rw-r--r--  1 root     root         8260 Nov 27 14:11  ./visitor_analytics/visitor_log/app.js
-rw-r--r--  1 root     root          609 Sep 21 22:49  ./visitor_analytics/visitor_log/favicon.svg
-rw-r--r--  1 root     root         3651 Nov 27 14:11  ./visitor_analytics/visitor_log/index.html
-rw-r--r--  1 root     root         3331 Nov 27 14:11  ./visitor_analytics/visitor_log/styles.css


#Apache setup is as follows
root: sites-enabled# cat tglauner-ssl.conf 
<VirtualHost *:443>
        ServerAdmin glaunertim@gmail.com

        DocumentRoot /var/www/html
        <Directory /var/www/html>
                AllowOverride All
                Require all granted
                Options -Indexes
        </Directory>

        # Git and sensitive files and dirs hardening
        <DirectoryMatch "^/.*/\.git/">
                Require all denied
        </DirectoryMatch>

        <FilesMatch "^\.git">
                Require all denied
        </FilesMatch>

        <FilesMatch "\.(sh|py|pl|bak|old|log|ini|conf|csv)$">
                Require all denied
        </FilesMatch>

        # App multi_model_talkshow
        ProxyPreserveHost On
        ProxyPass /multi_model_talkshow/api http://127.0.0.1:8002/api
        ProxyPassReverse /multi_model_talkshow/api http://127.0.0.1:8002/api

        Alias /multi_model_talkshow/ /var/www/html/multi_model_talkshow/frontend/dist/
        <Directory /var/www/html/multi_model_talkshow/frontend/dist>
                Require all granted
                Options -Indexes
                DirectoryIndex index.html
                RewriteEngine On
                RewriteCond %{REQUEST_FILENAME} !-f
                RewriteCond %{REQUEST_FILENAME} !-d
                RewriteRule ^ index.html [L]
        </Directory>

        # App dashboard
        Alias /dashboard/ /var/www/html/dashboard/dist/

        <Directory /var/www/html/dashboard/dist>
            Options -Indexes +FollowSymLinks -MultiViews
            AllowOverride All
            Require all granted

            # Always prefer index.html here         
            DirectoryIndex index.html

            # For Single Page Applications (SPAs) like React, rewrite all requests
            # within /dashboard/ to index.html if the file doesn't exist.
            RewriteEngine On
            RewriteCond %{REQUEST_FILENAME} !-f
            RewriteCond %{REQUEST_FILENAME} !-d
            RewriteRule . index.html [L]
        </Directory>

        #LogLevel info ssl:warn

        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined

        #   SSL Engine Switch:
        SSLEngine on

        <FilesMatch "\.(?:cgi|shtml|phtml|php)$">
                SSLOptions +StdEnvVars
        </FilesMatch>
        <Directory /usr/lib/cgi-bin>
                SSLOptions +StdEnvVars
        </Directory>

        ServerName      tglauner.com
        Include   /etc/letsencrypt/options-ssl-apache.conf
        ServerAlias www.tglauner.com
        SSLCertificateFile /etc/letsencrypt/live/tglauner.com/fullchain.pem
        SSLCertificateKeyFile /etc/letsencrypt/live/tglauner.com/privkey.pem

        # App visitor_analytics
        ProxyPreserveHost On
        ProxyPass        /api/     http://127.0.0.1:9000/api/
        ProxyPassReverse /api/     http://127.0.0.1:9000/api/
        ProxyPass        /collect  http://127.0.0.1:9000/collect
        ProxyPassReverse /collect  http://127.0.0.1:9000/collect
        ProxyPass        /healthz http://127.0.0.1:9000/healthz
        ProxyPassReverse /healthz http://127.0.0.1:9000/healthz

        Alias /visitor_log/ "/var/www/html/visitor_analytics/visitor_log/"
        <Directory "/var/www/html/visitor_analytics/visitor_log">
                Options -Indexes
                Require all granted
        </Directory>
        RewriteEngine On
        RewriteCond %{REQUEST_URI} ^/visitor_log/
        RewriteCond %{REQUEST_FILENAME} !-f
        RewriteCond %{REQUEST_FILENAME} !-d
        RewriteRule ^visitor_log/ /visitor_log/index.html [L]

        Alias /js/ "/var/www/html/visitor_analytics/tracking/"
        <Directory "/var/www/html/visitor_analytics/tracking">
                Options -Indexes
                Require all granted
        </Directory>

        # App ai_value_advisor
        ProxyPreserveHost On
        ProxyPass        /ai_value_advisor/api/ http://127.0.0.1:8001/api/
        ProxyPassReverse /ai_value_advisor/api/ http://127.0.0.1:8001/api/

        Alias /ai_value_advisor/ /var/www/html/ai_value_advisor/frontend/dist/

        <Directory /var/www/html/ai_value_advisor/frontend/dist/>
                Require all granted
                Options -Indexes
                DirectoryIndex index.html

                # SPA fallback (Apache 2.4+)
                FallbackResource index.html
        </Directory>

        # Allow .py file to be downloaded explicitly
        <Directory "/var/www/html/frtb_fundamentals">
        # Make sure .py is treated as a normal static file, not CGI
                RemoveHandler .py
                <FilesMatch "\.py$">
                        Require all granted
                </FilesMatch>
        </Directory>

        # Protect mcp server from direct acccess
        <Directory /var/www/html/mcp.tglauner.com>
                Require all denied
        </Directory>
        # MCP Reverse Proxy 
        ProxyPreserveHost On
        ProxyPass /mcp http://127.0.0.1:3000/mcp flushpackets=on
        ProxyPassReverse /mcp http://127.0.0.1:3000/mcp
</VirtualHost>

# Connect from mac mini to digitalocean droplet:
Copy stuff from Mac to Digitalocean
Folder (recursive)
scp -r /path/on/mac/mydir root@45.55.196.120:/var/www/html/
Single file
scp /path/on/mac/file.html root@45.55.196.120:/var/www/html/
Other commands probably work similarly

# Config files on droplet
/etc/apache2/sites-enabled/tglauner-ssl.conf
/etc/systemd/system/ai-value-advisor.service
