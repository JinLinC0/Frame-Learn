import { Module } from '@nestjs/common';
import { JwdService } from './jwd.service';
import { JwdController } from './jwd.controller';
import { JwtModule } from '@nestjs/jwt';
import { ConfigModule, ConfigService } from '@nestjs/config';
import { JwtStrategy } from './jwt.strategy';

@Module({
  imports: [
    // 注册jwt模块
    JwtModule.registerAsync({
      // 引入配置模块和服务
      imports: [ConfigModule],
      inject: [ConfigService],
      // 编写一个工厂函数，将服务实例引入，后续在工厂函数内部就可以使用configService来获取配置文件中的配置项
      useFactory: (config: ConfigService) => {
        return {
          secret: config.get('TOKEN_SECRET'), // 读取并设置token的密钥
          signOptions: { expiresIn: '100d' }  // 设置token过期时间:100天
        }
      }
    })
  ],
  providers: [JwdService, JwtStrategy],
  controllers: [JwdController]
})
export class JwdModule {}
