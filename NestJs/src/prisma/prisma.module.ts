import { Global, Module } from '@nestjs/common';
import { PrismaService } from './prisma.service';

// 将模块变成全局，并且将服务暴露出去
@Global()
@Module({
  providers: [PrismaService],
  exports: [PrismaService],
})
export class PrismaModule {}
