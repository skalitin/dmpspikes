var models = {

    "ad_field": {
        "type": "ad_fields",
        "fields": {
            "projectId": {
                "type": "string",
                "index": false
            },
            "title": {
                "type": "string"
            },
        }
    },

    "backup": {
        "type": "backups",
        "fields": {
            "tenantId": {
                "type": "string"
            },
            "projectId": {
                "type": "string",
                "index": false
            },
            "title": {
                "type": "string"
            },
            "when": {
                "type": "date"
            },
            "users": {
                "type": "long"
            },
            connectionId: {
		 type: "string" 
	    },
            collections: {
                type: "array",
                element: {
                    id: { type: "string", index: false }
                }
            }

        }
    },

    "task": {
        "fields": {
            "backup": {
                "type": "string"
            }
        }
    },

    "object": {
        "fields": {
            "displayName": {
                "type": "string"
            },
            "givenName": {
                "type": "string"
            },
            "surname": {
                "type": "string"
            },
            "mail": {
                "type": "string"
            },
            "mailNickname": {
                "type": "string"
            },
            "backupDate": {
                "type": "date"
            },
            "tenantId": {
                "type": "string"
            },
        }
    },

    "connection": {
       "fields": {
            "tenantId": {
                "type": "string"
            },	
            "clientId": {
                "type": "string"
            },	
            "clientSecret": {
                "type": "string"
            },	
	    }
    }
}

module.exports = models;
