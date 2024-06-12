import fs from 'fs';
import path from 'path';
import express, { Request as Req, Response as Res, NextFunction as Next } from 'express';

type bool = boolean;
type str = string;

const Exp = express();

interface ClientsListed{
    ip:str,
    user_agent:str,
    requests:number,
    last_request:str
}

class Logs{
    private constructor(){}
    public static serverUp: str = "?";
    public static requests: str[] = [];
    public static update(): void{
        console.clear();
        console.log(Logs.serverUp);
        console.log("\nClients:");
        console.table(Clients.listed);
        console.log("\nLast requests:")
        for(let i = 5; i>0; i--){
            console.log(Logs.requests[Logs.requests.length - i]);
        }
    }
}


class Clients{
    private constructor(){}
    public static listed: ClientsListed[] = [];  
}

class Server{
    private constructor(){}
    private static readonly Port: number = 54321;
    private static isActive: bool = false;
    private static allowHttpMethods(req: Req, res: Res, next: Next): any{
        if (req.method !== 'GET'){
            return res.status(405).send("Error 405 - Method not allowed");
        }
        next();
    }
    private static aboutRequest(req: Req, res: Res, next: Next): void{
        const ip = `${req.ip}`;
        const userAgent = `${req.get("User-Agent")}`;
        const lastRequest = `${req.method} -> ${req.url}`;
        Logs.requests.push(`${ip} : ${lastRequest}`);
        let unlisted = true;
        for (let i = 0; i < Clients.listed.length; i++){
            if (Clients.listed[i].ip === ip){
                unlisted = false;
                Clients.listed[i].requests++;
                Clients.listed[i].last_request = lastRequest;
                break;
            }
        }
        if (unlisted){
            Clients.listed.push({ "ip": ip, "user_agent": userAgent, "requests": 1, "last_request": lastRequest });
        }
        Logs.update();
        next();
    }
    public static init(): void{
        if (!Server.isActive && Exp !== null){
            Server.isActive = true;
            Exp.use(Server.allowHttpMethods)
            Exp.use(Server.aboutRequest);
            Exp.use("/", express.static(path.join(__dirname, "../public")));
            Exp.get("/", (req, res) => {
                res.sendFile(path.join(__dirname, "../public", "index.html"));
            });
            Exp.listen(Server.Port, () => {
                Logs.serverUp = `Servidor rodando em http://localhost:${Server.Port}`;
                console.log(Logs.serverUp);
            });
        }
    }
}

function init(): void{
    Server.init();
}

module.exports = {init};
