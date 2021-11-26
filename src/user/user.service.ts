import { InjectModel } from '@nestjs/mongoose';
import { Injectable, NotFoundException } from '@nestjs/common';
import { Model } from 'mongoose';
import { User } from './User.model';

@Injectable()
export class UserService {
  private Users: User[] = [];

  constructor(
    @InjectModel('Users') private readonly userModel: Model<User>,
  ) {}

  async insertUser( usernamee: string, password: string) {
    const newUser = new this.userModel();
    newUser.username = usernamee;
    newUser.password = password;
    newUser.updateAt = new Date();
    const result = await newUser.save();
    return result.id as string;
  }

  async editUser(
    id: string,
    username: string,
    password: string,
  ) {
    const update =await this.userModel.findById(id);
    update.updateAt = new Date();
    update.password = password;
    update.save();
  }
  async getSingUser(UserId: string){
    const result = await this.userModel.findById(UserId);
    return {
        username: result.username,
        password: result.password, 
        updateAt: result.updateAt,
        id: result.id,
    }
  }
  async deleteUser(UserId: string){
    await this.userModel.deleteOne({_id: UserId}).exec();
  }
  async getUsers() {
    const Users = await this.userModel.find().exec();
    //console.log(result);
    return Users.map((prod) => ({
        username: prod.username,
        password: prod.password,
        updateAt: prod.updateAt,
      id: prod.id,
    }));
  }
  // private async findUser(id: string): Promise<Model<User>> {
  //   let User;
  //   try{
  //     User = await this.UserModel.findById(id);
  //   } catch(error){
  //     throw new NotFoundException('khong tim thay');
  //   }
  //   if(!User) throw new NotFoundException('khong tim thay');
  //   return User;
  // }
}
