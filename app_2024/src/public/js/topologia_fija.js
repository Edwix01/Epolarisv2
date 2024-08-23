

var topologyData = {
    "links": [
        {
            "id": 0,
            "index": 1,
            "port_bloks": false,
            "port_blokt": true,
            "source": 0,
            "srcDevice": "10.0.1.1",
            "srcIfName": "G0/2",
            "target": 1,
            "tgtDevice": "10.0.1.2",
            "tgtIfName": "G0/2"
        },
        {
            "id": 1,
            "index": 1,
            "port_bloks": false,
            "port_blokt": false,
            "source": 1,
            "srcDevice": "10.0.1.2",
            "srcIfName": "G0/3",
            "target": 3,
            "tgtDevice": "10.0.1.4",
            "tgtIfName": "G0/2"
        },
        {
            "id": 2,
            "index": 2,
            "port_bloks": false,
            "port_blokt": true,
            "source": 1,
            "srcDevice": "10.0.1.2",
            "srcIfName": "G1/0",
            "target": 3,
            "tgtDevice": "10.0.1.4",
            "tgtIfName": "G0/3"
        },
        {
            "id": 3,
            "index": 1,
            "port_bloks": false,
            "port_blokt": false,
            "source": 2,
            "srcDevice": "10.0.1.3",
            "srcIfName": "G0/2",
            "target": 0,
            "tgtDevice": "10.0.1.1",
            "tgtIfName": "G0/3"
        },
        {
            "id": 4,
            "index": 1,
            "port_bloks": false,
            "port_blokt": false,
            "source": 2,
            "srcDevice": "10.0.1.3",
            "srcIfName": "G0/3",
            "target": 1,
            "tgtDevice": "10.0.1.2",
            "tgtIfName": "G1/1"
        },
        {
            "id": 5,
            "index": 1,
            "port_bloks": false,
            "port_blokt": false,
            "source": 2,
            "srcDevice": "10.0.1.3",
            "srcIfName": "G1/0",
            "target": 4,
            "tgtDevice": "10.0.1.5",
            "tgtIfName": "G0/2"
        }
    ],
    "nodes": [
        {
            "IP": "10.0.1.1",
            "icon": "switch",
            "id": 0,
            "layerSortPreference": 2,
            "marca": "CISCO",
            "name": "S1"
        },
        {
            "IP": "10.0.1.2",
            "icon": "switch",
            "id": 1,
            "layerSortPreference": 2,
            "marca": "CISCO",
            "name": "S2"
        },
        {
            "IP": "10.0.1.3",
            "icon": "switch",
            "id": 2,
            "layerSortPreference": 1,
            "marca": "CISCO",
            "name": "S3"
        },
        {
            "IP": "10.0.1.4",
            "icon": "switch",
            "id": 3,
            "layerSortPreference": 3,
            "marca": "CISCO",
            "name": "S4"
        },
        {
            "IP": "10.0.1.5",
            "icon": "switch",
            "id": 4,
            "layerSortPreference": 2,
            "marca": "CISCO",
            "name": "S5"
        }
    ]
};