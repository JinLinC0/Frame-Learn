import { Body, Controller, Post } from '@nestjs/common';
import { LoginService } from './login.service';
import RegisterDto from './dto/register.dto';
import Login2Dto from './dto/login2.dto';

@Controller('login')
export class LoginController {
    // 将服务进行依赖注入
    constructor(private readonly login: LoginService) {}
    // 注册
    @Post('register')
    register(@Body() dto: RegisterDto) {
        return this.login.register(dto);
    }

    // 登录
    @Post('login2')
    login2(@Body() dto: Login2Dto) {
        return this.login.login2(dto);
    }
}
