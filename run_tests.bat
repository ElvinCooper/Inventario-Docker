@echo off
REM Script para ejecutar tests en Windows
REM Uso: run_tests.bat [unit|integration|fast|parallel]

echo ================================
echo    Test Suite - Inventory API
echo ================================
echo.

REM Limpiar contenedores anteriores
echo  Limpiando contenedores anteriores...
docker-compose -f docker-compose.test.yaml down -v 2>nul

REM Iniciar base de datos de pruebas
echo  Iniciando PostgreSQL para tests...
docker-compose -f docker-compose.test.yaml up -d

REM Esperar a que PostgreSQL esté listo
echo  Esperando a que PostgreSQL esté listo...
timeout /t 5 /nobreak >nul

REM Verificar que el contenedor está corriendo
docker ps | findstr inventory_test_db >nul
if errorlevel 1 (
    echo  Error: El contenedor de PostgreSQL no está corriendo
    pause
    exit /b 1
)

echo  PostgreSQL listo!
echo.

REM Ejecutar tests según el argumento
if "%1"=="unit" (
    echo Ejecutando solo tests unitarios...
    pytest tests/ -v -m unit --cov=app --cov-report=term-missing --cov-report=html
) else if "%1"=="integration" (
    echo Ejecutando solo tests de integración...
    pytest tests/ -v -m integration --cov=app --cov-report=term-missing --cov-report=html
) else if "%1"=="fast" (
    echo Ejecutando tests en modo rápido...
    pytest tests/ -v --tb=short
) else if "%1"=="parallel" (
    echo Ejecutando tests en paralelo...
    pytest tests/ -v -n auto --cov=app --cov-report=term-missing --cov-report=html
) else (
    echo Ejecutando todos los tests...
    pytest tests/ -v --cov=app --cov-report=term-missing --cov-report=html
)

REM Guardar el código de salida
set TEST_EXIT_CODE=%errorlevel%

REM Detener contenedor
echo.
echo Deteniendo PostgreSQL...
docker-compose -f docker-compose.test.yaml down -v

REM Mostrar resultado final
echo.
echo ================================
if %TEST_EXIT_CODE% equ 0 (
    echo  Todos los tests pasaron!
    echo Reporte de coverage: htmlcov\index.html
) else (
    echo  Algunos tests fallaron
)
echo ================================

pause
exit /b %TEST_EXIT_CODE%
```

---

