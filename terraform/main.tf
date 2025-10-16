resource "aws_sqs_queue" "orders" {
  name                      = "orders-queue"
  visibility_timeout_seconds = 30
  redrive_policy            = jsonencode({ deadLetterTargetArn = aws_sqs_queue.dlq.arn, maxReceiveCount = 5 })
}
resource "aws_sqs_queue" "dlq" { name = "orders-dlq" }

resource "aws_sns_topic" "shipments" { name = "shipments-topic" }

resource "aws_s3_bucket" "labels" {
  bucket        = "tf-orders-labels"
  force_destroy = true
}

resource "aws_dynamodb_table" "orders" {
  name         = "orders"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "order_id"
  attribute { name = "order_id"; type = "S" }
}
output "orders_queue_url"     { value = aws_sqs_queue.orders.id }
output "shipments_topic_arn"  { value = aws_sns_topic.shipments.arn }
output "labels_bucket"        { value = aws_s3_bucket.labels.bucket }
output "orders_table"         { value = aws_dynamodb_table.orders.name }
