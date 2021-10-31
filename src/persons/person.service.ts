import { InjectModel } from '@nestjs/mongoose';
import { Injectable, NotFoundException } from '@nestjs/common';
import { Model } from 'mongoose';
import { Person } from './person.model';

@Injectable()
export class PersonService {
  private persons: Person[] = [];

  constructor(
    @InjectModel('Persons') private readonly personModel: Model<Person>,
  ) {}

  async insertPerson(Fname: string, Lname: string, Status: Boolean) {
    const newPerson = new this.personModel({
      Fname,
      Lname,
      Status,
    });
    const result = await newPerson.save();
    return result.id as string;
  }

  async editPerson(
    personId: string,
    Fname: string,
    Lname: string,
    Status: Boolean,
  ) {
    const update =await this.personModel.findById(personId);
    update.Status = Status;
    update.Fname = Fname;
    update.Lname = Lname;
    update.save();
  }
  async getSingPerson(personId: string){
    const result = await this.personModel.findById(personId);
    return {
      id: result.id,
      Fname: result.Fname,
      Lname: result.Lname,
      Status: result.Status,

    }
  }
  async deletePerson(personId: string){
    await this.personModel.deleteOne({_id: personId}).exec();
  }
  async getPersons() {
    const persons = await this.personModel.find().exec();
    //console.log(result);
    return persons.map((prod) => ({
      id: prod.id,
      Fname: prod.Fname,
      Lname: prod.Lname,
      Status: prod.Status,
    }));
  }
  // private async findPerson(id: string): Promise<Model<Person>> {
  //   let person;
  //   try{
  //     person = await this.personModel.findById(id);
  //   } catch(error){
  //     throw new NotFoundException('khong tim thay');
  //   }
  //   if(!person) throw new NotFoundException('khong tim thay');
  //   return person;
  // }
}
