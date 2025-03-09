import { BadRequestException, Injectable } from '@nestjs/common';
import RegisterDto from './dto/register.dto';
import { PrismaService } from './../prisma/prisma.service';
import { hash, verify } from 'argon2';
import { JwtService } from '@nestjs/jwt';
import { User } from '@prisma/client';
import LoginDto from './dto/login.dto';

@Injectable()
export class JwdService {
    // 依赖注入，拿取prisma服务
    constructor(
        private readonly prisma: PrismaService,
        private jwt: JwtService
    ) {}
    // 注册用户
    async register(dto: RegisterDto) {
        const user = await this.prisma.user.create({
            data: {
                name: dto.name,
                password: await hash(dto.password),  // 密码加密
                email: dto.email
            }
        })
        return this.token(user)
    }

    // 生成token   User为prisma中定义的User类型
    async token({ name, id }: User) {
        // 使用jwt服务生成签名
        return {
            token: await this.jwt.signAsync({ 
                // 将要存储的内容放入
                name,
                sub: id   // 后续就可以根据这个token值得到这个id，通过这个id查找到用户
            })
        }
    }

    // 登录用户服务
    async login(dto: LoginDto) {
        // 去数据库中查找用户的name是否存在
        const user = await this.prisma.user.findFirst({
            where: {
                name: dto.name,
            }
        })
        // 密码验证
        // 对加密的密码进行解密   verify(加密的密码，提交过来的密码)
        if (!user) {
            throw new BadRequestException('用户名不存在');
        }
        if (!(await verify(user.password, dto.password))) {
            throw new BadRequestException('密码输入错误');
        }
        return this.token(user);
    }

    // 查询所有用户
    async findAll() {
        return this.prisma.user.findMany();
    }
}
