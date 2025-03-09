import { DynamicModule, Module } from '@nestjs/common';
import { ConfigService } from './config.service';

@Module({
  providers: [ConfigService],
  exports: [ConfigService],
})

export class ConfigModule {
    static forRoot(options: { path: string }): DynamicModule {
        return {
            global: true,
            module: ConfigModule,    // 模块必须加上
            providers: [{ provide: 'CONFIG_OPTIONS', useValue: options }],  // 定义一个服务
        }
    }
}