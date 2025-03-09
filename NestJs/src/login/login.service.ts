import { BadRequestException, Injectable, NotFoundException } from '@nestjs/common';
import { PrismaService } from 'src/prisma/prisma.service';
import RegisterDto from './dto/register.dto';
import { hash, verify } from 'argon2';
import Login2Dto from './dto/login2.dto';

@Injectable()
export class LoginService {
    // 注入PrismaService服务
    constructor(private prisma: PrismaService) { }
    // 注册服务
    // 在服务中完善注册函数，提供给控制器使用，注册要提供注册的数据
    async register(dto: RegisterDto) {
        // 对密码进行加密
        const password = await hash(dto.password);
        // 使用查询构造器将内容提交到数据库
        const user = await this.prisma.user.create({
            data: {
                name: dto.name,
                password: password,
                email: dto.email,
                github: dto.github,
                avatar: dto.avatar,
            }
        });
        return user;
    }

    // 登录服务
    async login2(dto: Login2Dto) {
        const user = await this.prisma.user.findFirst({
            where: {
                name: dto.name
            }
        });
        // 如果用户不存在，抛出异常
        if (!user) {
            throw new NotFoundException('用户不存在');
        }
        // 检查 dto.password 是否存在
        if (!dto.password) {
            throw new BadRequestException('密码不能为空');
        }
        // 使用校对方法verify对密码进行校对
        // 如果校对失败，提示密码输入错误
        if (! await verify(user.password, dto.password)) {
            throw new BadRequestException('密码输入错误');
        }

        return user;
    }
}
