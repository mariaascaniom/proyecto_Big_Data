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