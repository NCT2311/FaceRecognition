import { Module } from "@nestjs/common";
import {MongooseModule  } from "@nestjs/mongoose";
import { Flagschema } from "src/flag/flag.model";
import { FlagModule } from "src/flag/flag.module";
import { FlagService } from "src/flag/flag.service";
import { TurnController } from "./turn.controller";
import {Turnschema} from "./turn.model";
import { TurnService } from "./turn.service";

 
@Module({
    imports: [MongooseModule.forFeature([{name: 'turns', schema: Turnschema},{name: 'Flags', schema: Flagschema}])],
    controllers:[TurnController],
    providers: [TurnService,FlagService],
})
export class TurnModule{}