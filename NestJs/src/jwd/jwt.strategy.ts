import { Injectable } from "@nestjs/common";
import { PassportStrategy } from "@nestjs/passport";
import { ExtractJwt, Strategy, StrategyOptionsWithoutRequest } from "passport-jwt";
import { PrismaService } from "./../prisma/prisma.service";
import { ConfigService } from "@nestjs/config";

@Injectable()
export class JwtStrategy extends PassportStrategy(Strategy, 'jwt') {
    constructor(configService: ConfigService, private prisma: PrismaService) {
        super({
            // 解析用户提交的Bearer Token header数据，如果token有效，会自动调用validate方法，如果token是无效的，会自动抛出异常
            jwtFromRequest: ExtractJwt.fromAuthHeaderAsBearerToken(),
            // 告知加密使用的是哪个密钥，.env文件中的密钥配置
            secretOrKey: configService.get('TOKEN_SECRET'),
        } as StrategyOptionsWithoutRequest);
    }

    // 验证通过后（token有效）结果用户资料
    async validate({ sub: id }) {
        // 查询user表，得到这个token对应的用户，放到全局的Request.user中
        return this.prisma.user.findUnique({
            where: { id },
        })
    }
}