import { Body, Controller, Post } from '@nestjs/common';
import { AppService } from './app.service';
import { RequestPipe } from './request/request.pipe';
import CreateArticleDto from './dto/create.article.dto';
import { PrismaClient } from '@prisma/client';

@Controller()
export class AppController {
  prisma: PrismaClient;
  constructor(private readonly appService: AppService) {
    this.prisma = new PrismaClient();
  }

  @Post('store')
  async add(@Body() dto: CreateArticleDto) {
    await this.prisma.article.create({
        data: {
            title: dto.title,
            content: dto.content,
            thumb: "https://www.baidu.com",
            categoryId: 1,
        },
    });
  }
}