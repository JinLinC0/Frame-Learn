import { Body, Controller, Get, Post, Req } from '@nestjs/common';
import { JwdService } from './jwd.service';
import RegisterDto from './dto/register.dto';
import LoginDto from './dto/login.dto';
import { Auth } from './decorator/jwd.decorator';
import { User } from './decorator/user.decorator';
import { User as UserEntity } from '@prisma/client';

@Controller('jwd')
export class JwdController {
    // 将服务的依赖注入
    constructor(private readonly jwd: JwdService) {}

    // 写一个注册路由
    @Post('register')
    // 接收注册提交的表单数据
    register(@Body() dto: RegisterDto) {
        return this.jwd.register(dto);
    }

    // 登录路由
    @Post('login')
    // 接收登录提交的表单数据
    login(@Body() dto: LoginDto) {
        return this.jwd.login(dto);
    }

    // 获取所有用户
    @Get('all')
    @Auth()
    all(@User() user: UserEntity) {
        // 得到当前操作的用户req.user
        return user
    }
}
