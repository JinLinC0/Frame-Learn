import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
// import { ConfigModule } from './config/config.module';
import { AuthModule } from './auth/auth.module';
import { LoginModule } from './login/login.module';
import { PrismaModule } from './prisma/prisma.module';
import { JwdModule } from './jwd/jwd.module';
import path from 'path';
import { ConfigModule } from '@nestjs/config';
import { UploadModule } from './upload/upload.module';

// const configPath = path.resolve(__dirname, './configure')
@Module({
  imports: [ConfigModule.forRoot( { isGlobal: true } ), AuthModule, LoginModule, PrismaModule, JwdModule, UploadModule],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}
