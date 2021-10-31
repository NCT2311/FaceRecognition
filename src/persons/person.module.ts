import { Module } from "@nestjs/common";
import {MongooseModule  } from "@nestjs/mongoose";
import { PersonController } from "./person.controller";
import {Personschema} from "./person.model";
import { PersonService } from "./person.service";

 
@Module({
    imports: [MongooseModule.forFeature([{name: 'Persons', schema: Personschema}])],
    controllers:[PersonController],
    providers: [PersonService],
})
export class PersonModule{}