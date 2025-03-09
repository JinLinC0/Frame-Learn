import { Injectable } from '@nestjs/common';
import { PrismaClient } from '@prisma/client';

@Injectable()
export class PrismaService extends PrismaClient {
    constructor() {
        // 会打印出我们的查询日志
        super({ log: ['query'] })
    }
}
