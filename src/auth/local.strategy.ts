

import { Injectable, UnauthorizedException } from '@nestjs/common';
import { PassportStrategy } from '@nestjs/passport';
import { Strategy } from 'passport-local';
import * as bcrypt from 'bcrypt'; 
import { UserService } from 'src/user/user.service';


@Injectable()
export class LocalStrategy extends PassportStrategy(Strategy) {
    constructor( private userService: UserService) {
        super({
            usernameField: 'username'
        });
    }
//Authentication : Xác Thực   
//Authorication: Xác Nhận
    async validate(username: string, password: string) {
        let student = await this.userService.getUsers();
        let user;
        for (var i = 0 ; i < student.length ; i++){
            if (student[i].username == username) {
                user = student[i];
            }
        }
        // console.log(user);
        if (!user) throw new UnauthorizedException("Không tồn tại tài khoản này");
        if (!(await bcrypt.compare(password, user.password))) throw new UnauthorizedException("Sai tài khoản hoặc mật khẩu");
        return { //Return 1 cái json
            username: user.username
        };
    }
}
