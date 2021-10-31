
import { InjectModel } from '@nestjs/mongoose';
import { Injectable } from '@nestjs/common';
import { Model } from 'mongoose';
import { Person } from './person.model';

@Injectable()
export class PersonService {
  private persons: Person[] = [];

  constructor(
    @InjectModel('Persons') private readonly personModel: Model<Person>,
  ) {}

  async insertPerson(
    id: Number,
    Fname: string,
    Lname: string,
    Status: Boolean,
  ) {
    const newPerson = new this.personModel({
      id,
      Fname,
      Lname,
      Status,
    });
    const result = await newPerson.save();
    return result.id as string;
  }

  async editPerson(person: Person) {
    this.personModel.updateOne(person);
  }
  async getPersons(){
    const result  = await this.personModel.find();
    //console.log(result);
    return [...result];
  }
}
