from pysnmp.entity.rfc3413.oneliner import cmdgen

cmdGen = cmdgen.CommandGenerator()
def obtr(direc,datos,ipstplink):
    ro_tplink = ""
    f = 0
    br_id = {}
    fif = {}
    stpinfo = {}
    db = []
    pd = []

    #Obtener el root de tplink
    if len(ipstplink) > 0:
        ip = ipstplink[0]
        comunidad = datos[ip]["snmp"]
        # Realizar la solicitud SNMP para obtener estadísticas
        errorIndication, errorStatus, errorIndex, varBindTable = cmdGen.bulkCmd(
            cmdgen.CommunityData(comunidad),
            cmdgen.UdpTransportTarget((ip, 161)),
            0, 5,
            '1.3.6.1.2.1.17.2.5'
        )

        # Procesar los resultados
        if errorIndication:
            f = 1
            fif[ip] = ""

            print(f"Error: {errorIndication}")
        else:
            ro_tplink =  ((varBindTable[0][0][1]).prettyPrint())[-12:]


    #Inicia Proceso para recuperar Bridge ID
    for server_ip in direc:
        comunidad = datos[server_ip]["snmp"]
        errorIndication, errorStatus, errorIndex, varBindTable = cmdGen.bulkCmd(
            cmdgen.CommunityData(comunidad),
            cmdgen.UdpTransportTarget((server_ip, 161)),
            0,5,
            '1.3.6.1.2.1.17.1.1'
        )
        if errorIndication:
            f = 1
            fif[server_ip] = ""
            print(f"Error: {errorIndication}")
        else:
            br_id[server_ip] =  ((varBindTable[0][0][1]).prettyPrint())[-12:]


        #Inicia Proceso para obtener stp info
        errorIndication, errorStatus, errorIndex, varBindTable = cmdGen.bulkCmd(
        cmdgen.CommunityData(comunidad),
        cmdgen.UdpTransportTarget((server_ip, 161)),
        0,25,
        '1.3.6.1.2.1.17.2.15.1.8'
        )
        if errorIndication:
            f = 1
            fif[server_ip] = ""
            print(f"Error: {errorIndication}")
        else:
            db.append(((varBindTable[0][0][1]).prettyPrint())[-12:])


        errorIndication1, errorStatus1, errorIndex1, varBindTable1 = cmdGen.bulkCmd(
            cmdgen.CommunityData(comunidad),
            cmdgen.UdpTransportTarget((server_ip, 161)),
            0,25,
            '1.3.6.1.2.1.17.2.15.1.9'
        )
        for varBindTableRow1 in varBindTable1:
            for name1, val1 in varBindTableRow1:
                pd.append((str(name1).split(".")[-1], (val1.prettyPrint())[-12:]))
        if errorIndication1:
            f = 1
            fif[server_ip] = ""
            print(f"Error: {errorIndication1}")
        else:
            stpinfo[server_ip] = [db,pd]

    return ro_tplink,br_id,stpinfo,f,fif

