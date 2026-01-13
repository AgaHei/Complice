@echo off
chcp 65001 >nul
title Lancement de Complice
color 0A

echo.
echo ████████████████████████████████████████
echo █                                      █
echo █        🚀 LANCEMENT COMPLICE         █
echo █     Application d'aide à l'autisme   █
echo █                                      █
echo ████████████████████████████████████████
echo.

:: Changer vers le dossier du projet
cd /d "%~dp0"

echo [%time%] 🔍 Verification de Docker Desktop...
:: Vérifier si Docker Desktop est en cours d'exécution
docker version >nul 2>&1
if errorlevel 1 (
    echo.
    echo ❌ ERREUR: Docker Desktop n'est pas demarre !
    echo.
    echo 💡 SOLUTION:
    echo    1. Ouvrez Docker Desktop depuis le menu Demarrer
    echo    2. Attendez qu'il soit completement demarre
    echo    3. Relancez ce script
    echo.
    pause
    exit /b 1
)
echo ✅ Docker Desktop est operationnel !

echo.
echo [%time%] 🐳 Demarrage de l'environnement Docker...
:: Démarrer les conteneurs en arrière-plan
docker-compose up -d
if errorlevel 1 (
    echo.
    echo ❌ ERREUR lors du demarrage des conteneurs !
    echo 💡 Tentative de reconstruction...
    docker-compose down
    docker-compose up -d --build
    if errorlevel 1 (
        echo.
        echo ❌ Impossible de demarrer l'environnement Docker.
        echo 💡 Verifiez que le fichier .env existe avec votre cle OpenAI.
        echo.
        pause
        exit /b 1
    )
)
echo ✅ Conteneur Docker demarre !

echo.
echo [%time%] ⏳ Attente de l'initialisation du conteneur...
:: Attendre que le conteneur soit prêt
timeout /t 5 /nobreak >nul

echo.
echo [%time%] 🧠 Arret des anciens processus Streamlit...
:: Nettoyer les processus Streamlit existants
docker exec complice-dev pkill -f streamlit >nul 2>&1

echo.
echo [%time%] 🚀 Lancement de l'application Complice...
:: Lancer Streamlit en arrière-plan
start /b "" docker exec complice-dev streamlit run /home/jovyan/work/interface/app.py --server.port 8501 --server.address 0.0.0.0

echo ✅ Application en cours de demarrage...

echo.
echo [%time%] ⏳ Initialisation de l'application (30 secondes)...
echo 📚 Chargement de la base de connaissances...
echo 🧠 Preparation de l'intelligence artificielle...

:: Barre de progression simulée
for /l %%i in (1,1,30) do (
    <nul set /p "=█"
    timeout /t 1 /nobreak >nul
)

echo.
echo.
echo ✅ Complice est pret !

echo.
echo [%time%] 🌐 Ouverture du navigateur web...
:: Ouvrir le navigateur après un petit délai
timeout /t 2 /nobreak >nul
start http://localhost:8501

echo.
echo ████████████████████████████████████████
echo █                                      █
echo █            ✅ SUCCES !               █
echo █                                      █
echo █  🌐 Application ouverte dans le      █
echo █     navigateur : localhost:8501     █
echo █                                      █
echo █  Pour fermer l'application:         █
echo █  Double-cliquez sur "Arreter        █
echo █  Complice" ou fermez cette fenetre  █
echo █                                      █
echo ████████████████████████████████████████
echo.

echo 💡 CONSEIL: Laissez cette fenetre ouverte pendant l'utilisation
echo 💡 Pour redemarrer: fermez le navigateur et relancez ce script
echo.

echo Appuyez sur une touche pour fermer cette fenetre et arreter l'application...
pause >nul

echo.
echo [%time%] 🛑 Arret de l'application...
docker exec complice-dev pkill -f streamlit >nul 2>&1
docker-compose down
echo ✅ Application fermee !
timeout /t 2 /nobreak >nul