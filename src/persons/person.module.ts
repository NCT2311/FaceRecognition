import { Module } from "@nestjs/common";
import {MongooseModule  } from "@nestjs/mongoose";
import { Turnschema } from "src/turns/turn.model";
import { TurnService } from "src/turns/turn.service";
import { AllhistoryController } from "./allhistory.controller";
import { HistoryController } from "./history.controller";
import { PersonController } from "./person.controller";
import {Personschema} from "./person.model";
import { PersonService } from "./person.service";
import { ThongkeController } from "./thongke.controller";

 
@Module({
    imports: [MongooseModule.forFeature([{name: 'Persons', schema: Personschema},{name: 'turns', schema: Turnschema}])],
    controllers:[PersonController,HistoryController,AllhistoryController,ThongkeController],
    providers: [PersonService, TurnService],
})
export class PersonModule{}