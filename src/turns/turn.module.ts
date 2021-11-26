import { Personschema } from './../persons/person.model';
import { PersonService } from './../persons/person.service';
import { Module } from "@nestjs/common";
import {MongooseModule  } from "@nestjs/mongoose";
import { Flagschema } from "src/flag/flag.model";
import { FlagModule } from "src/flag/flag.module";
import { FlagService } from "src/flag/flag.service";
import { TurnController } from "./turn.controller";
import {Turnschema} from "./turn.model";
import { TurnService } from "./turn.service";

 
@Module({
    imports: [MongooseModule.forFeature([{name: 'turns', schema: Turnschema},{name: 'Flags', schema: Flagschema},{name: 'Persons', schema: Personschema}])],
    controllers:[TurnController],
    providers: [TurnService,FlagService,PersonService],
})
export class TurnModule{}