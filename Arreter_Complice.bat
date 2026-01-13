@echo off
chcp 65001 >nul
title Arret de Complice
color 0C

echo.
echo ████████████████████████████████████████
echo █                                      █
echo █         🛑 ARRET COMPLICE            █
echo █     Application d'aide à l'autisme   █
echo █                                      █
echo ████████████████████████████████████████
echo.

:: Changer vers le dossier du projet
cd /d "%~dp0"

echo [%time%] 🛑 Arret de l'application Streamlit...
docker exec complice-dev pkill -f streamlit >nul 2>&1
if errorlevel 1 (
    echo ⚠️ Aucun processus Streamlit a arreter
) else (
    echo ✅ Application Streamlit arretee
)

echo.
echo [%time%] 🐳 Arret des conteneurs Docker...
docker-compose down
if errorlevel 1 (
    echo ❌ Erreur lors de l'arret des conteneurs
) else (
    echo ✅ Conteneurs Docker arretes
)

echo.
echo ████████████████████████████████████████
echo █                                      █
echo █            ✅ ARRETE !               █
echo █                                      █
echo █   L'application Complice a ete       █
echo █   fermee proprement.                 █
echo █                                      █
echo █   Pour relancer l'application:       █
echo █   Double-cliquez sur "Complice"      █
echo █   sur le Bureau                      █
echo █                                      █
echo ████████████████████████████████████████
echo.

echo Appuyez sur une touche pour fermer...
pause >nul