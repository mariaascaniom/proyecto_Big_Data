1. Historia de Usuario (HU-1)
    1.1. Como
        Manager del proyecto.
    1.2. Quiero
        Que las consultoras:
        • Conozcan el proyecto
        • Conozcan la herramienta TradingView
        • Conozcan sus fuentes de datos históricos:
        • https://github.com/ravalmeet/TradingView-Data/tree/master Este repositorio recoge
        la forma de obtener el histórico de los datos. La propuesta inicial es obtener 4 años
        con una frecuencia de 1 día
        • Conjunto de 10 criptomonedas objeto del proyecto:
            1. Bitcoin BTC
            2. Ethereum ETH
            3. Ripple XRP
            4. Solana SOL
            5. Dogecoin DOGE
            6. Cardano ADA
            7. Shiba Inu SHB
            8. Polkadot DOT
            9. Aave AAVE
            10. Stellar XLM
            1.3. Para
            Poder empezar con garantías el proyecto.


2. Historia de Usuario (HU-2)
    2.1. Como
        Manager del proyecto.
    2.2. Quiero
        Que las consultoras:
        • Creen el/los buckets necesarios en Amazon S3
        • Creen una primera jerarquía de carpetas
        • Definan el formato de los archivos de datos históricos que se van a almacenar en
        Amazon S3
        o Deben cargar todos los datos posibles, para que no tengan que volver a atrás en
        los sprint.
        o Deben hacerlo lo más genérico posible
        • Suban los primeros archivos en formato CSV
    2.3. Para
        Empezar a definir la capa de almacenamiento de datos históricos.
        

3. Historia de Usuario (HU-3)
    3.1. Como
        Manager del proyecto.
    3.2. Quiero
        Que las consultoras:
        • Utilicen el servicio AWS Glue Data Catalog y AWS Glue crawler para leer y guardar los
        metadatos relacionados con los datos históricos almacenados en S3
        o El nombre de la base datos debe tener la siguiente nomenclatura:
        § trade_data_<grupo> Ej: trade_data_imat3a01
        o El nombre de las tablas debe tener la siguiente nomenclatura (Puede haber una
        o varias tablas según el resultado de la HU-2)
        § trade_data_<tabla> Ej: trade_data_historico
        o Se deberá de hacer un script en python para automatizar la creación del
        catálogo de datos y la creación del crawler. Una vez hecho esto, habrá que hacer
        un push del código de python al repositorio de GitHub. La seguridad es un pilar
        fundamental para el cliente, por lo que el código que se suba a GitHub no deberá
        de contener ningún tipo de credencial.
    3.3. Para
        Realizar un gobierno de los datos almacenados en S3.