import { Controller, Get, Render,Post, Req ,Body, Res, UseGuards} from '@nestjs/common';
import { User } from './User.model';
import { UserService } from './User.service';
import * as bcrypt from 'bcrypt';
import { Request, Response } from 'express';
import { AuthGuard } from '@nestjs/passport';

@Controller('user')
export class UserController {
  constructor(private readonly userService: UserService) {}

    @Get()
    @UseGuards(AuthGuard('jwt'))
    @Render('user/index')
    async index() {
        const userlist = await this.userService.getUsers();
        //console.log(userlist);
        return {
            userlist: userlist
        };
    }
    @Post("add")
    @UseGuards(AuthGuard('jwt'))
    async add(@Body() user: User, @Res() res: Response): Promise<any> {
        // Hash: U -> K
        const salt = await bcrypt.genSalt(15);
        user.password = await bcrypt.hash(user.password, salt);
        await this.userService.insertUser(user.username, user.password);
        res.redirect("/user");
    }


    @Post("checkId")
    @UseGuards(AuthGuard('jwt'))
    async checkId(@Body('id') id: string) {
        let student = await this.userService.getUsers();
        for (var i = 0 ; i < student.length ; i++){
            if (student[i].username == id) return {
                  status: "FOUND"
            }
        }
        return {
            status: "NOT_FOUND"
        }
    }
    @Post("edit")
    @UseGuards(AuthGuard('jwt'))
    async edit(@Body() user: User,@Res() res: Response): Promise<any> {
        // console.log(user);
        let student = await this.userService.getUsers();
        for (var i = 0 ; i < student.length ; i++){
            if (student[i].username == user.username) {
                const salt = await bcrypt.genSalt(15);
                user.password = await bcrypt.hash(user.password, salt);
                await this.userService.editUser(student[i].id,user.username, user.password);
            }
        }
        res.redirect("/user");
    }
    @Post("delete")
    @UseGuards(AuthGuard('jwt'))
    async delete(@Body() user: User,@Res() res: Response): Promise<any> {
        let student = await this.userService.getUsers();
        for (var i = 0 ; i < student.length ; i++){
            if (student[i].username == user.username) {
                await this.userService.deleteUser(student[i].id);
            }
        }
        res.redirect("/user");
    }
    
}
