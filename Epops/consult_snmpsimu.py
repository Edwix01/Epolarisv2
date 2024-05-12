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
        errorIndication1, errorStatus1, errorIndex1, varBindTable1 = cmdGen.bulkCmd(
            cmdgen.CommunityData(comunidad),
            cmdgen.UdpTransportTarget((ip, 161)),
            0, 25,
            '1.3.6.1.2.1.17.2.5'
        )

        # Procesar los resultados
        if errorIndication1:
            f = 1
            fif[ip] = ""

            print(f"Error: {errorIndication1}")
        else:
            ro_tplink =  ((varBindTable1[0][0][1]).prettyPrint())[-12:]


    #Inicia Proceso para recuperar Bridge ID
    for server_ip in direc:
        comunidad = datos[server_ip]["snmp"]
        errorIndication2, errorStatus2, errorIndex2, varBindTable2 = cmdGen.bulkCmd(
            cmdgen.CommunityData(comunidad),
            cmdgen.UdpTransportTarget((server_ip, 161)),
            0,25,
            '1.3.6.1.2.1.2.2.1.6'
        )
        if errorIndication2:
            f = 1
            fif[server_ip] = ""
            print(f"Error: {errorIndication2}")
        else:
            br_id[server_ip] =  ((varBindTable2[0][0][1]).prettyPrint())[-12:]


        #Inicia Proceso para obtener stp info
        errorIndication3, errorStatus3, errorIndex3, varBindTable3 = cmdGen.bulkCmd(
        cmdgen.CommunityData(comunidad),
        cmdgen.UdpTransportTarget((server_ip, 161)),
        0,25,
        '1.3.6.1.2.1.17.2.15.1.8'
        )
        if errorIndication3:
            f = 1
            fif[server_ip] = ""
            print(f"Error: {errorIndication3}")
        else:
            db = list(map(lambda x: ((x[0][1]).prettyPrint())[-12:],varBindTable3))



        errorIndication4, errorStatus4, errorIndex4, varBindTable4 = cmdGen.bulkCmd(
            cmdgen.CommunityData(comunidad),
            cmdgen.UdpTransportTarget((server_ip, 161)),
            0,25,
            '1.3.6.1.2.1.17.2.15.1.9'
        )
        for varBindTableRow4 in varBindTable4:
            for name4, val4 in varBindTableRow4:
                pd.append((str(name4).split(".")[-1], (val4.prettyPrint())[-12:]))
        if errorIndication4:
            f = 1
            fif[server_ip] = ""
            print(f"Error: {errorIndication4}")
        else:
            stpinfo[server_ip] = [db,pd]

    return ro_tplink,br_id,stpinfo,f,fif

