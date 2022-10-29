[app]

# 애플리케이션 이름
title = 애니메이션 가사 퀴즈

# 패키지 이름
package.name = AnimeLyricsQuiz

# 패키지 도메인
package.domain = com.jeongjimin.animelyricsquiz

# main.py가 있는 소스 코드 폴더
source.dir = .

# 추가할 소스 파일들 (비워두면 모든 파일을 추가합니다)
source.include_exts = py,png,jpg,kv,atlas,ttf,csv

# 제외할 소스 파일들 (비워두면 아무 파일도 제외하지 않습니다)
source.exclude_exts = spec

# 제외할 폴더들 (비워두면 아무 폴더도 제외하지 않습니다)
source.exclude_dirs = tools

# 애플리케이션 버전
version = 0.1

# 애플리케이션 종속성
requirements = python3, kivy, kivymd==1.0.2, pygments, sdl2_ttf==2.0.15, pillow, docutils, plyer, discord-webhook, pandas, kivy_garden, requests, urllib3, charset-normalizer, idna, chardet, android, jnius, kivmob

# 애플리케이션의 스플래시 화면
presplash.filename = %(source.dir)s/data/presplash.png

# 애플리케이션의 아이콘
icon.filename = %(source.dir)s/data/icon.png

# 지원하는 각도 landscape, sensorLandscape, portrait 또는 all 중 하나)
orientation = portrait


# 필요없음 (ios지원 설정들)

osx.python_version = 3
osx.kivy_version = 1.9.1

# 필요없음 (ios지원 설정들)

#
# 안드로이드 설정
#

# 애플리케이션을 전체화면으로 실행할 것인지 아닌지
fullscreen = 0

# 안드로이드 권한들
android.permissions = INTERNET, ACCESS_NETWORK_STATE

# 빌드할 안드로이드 프로세서: armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = armeabi-v7a, arm64-v8a

# 안드로이드 오토 백업 활성화
android.allow_backup = True

# 릴리스 빌드 시 파일 확장자 (apk, aab 또는 aar)
android.release_artifact = aab

# 디버그 빌드 시 파일 확장자 (apk 또는 aar).
android.debug_artifact = apk

#
# Python for android (p4a) 설정
#

# python-for-android 브런치 설정 (기본은 master)
p4a.branch = master

# 안드로이드 빌드 시 사용할 부트스트랩
p4a.bootstrap = sdl2


#
# IOS 설정 (필요없음)
#


ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master
ios.ios_deploy_url = https://github.com/phonegap/ios-deploy
ios.ios_deploy_branch = 1.10.0
ios.codesign.allowed = false


[buildozer]

# 로그 단계 (0 = 에러만, 1 = 정보, 2 = 디버그 (명령어 출력과 함께))
log_level = 2

# 만약 buildozer가 root로 실행중일 시 경고 (0 = 거짓, 1 = 참)
warn_on_root = 0
